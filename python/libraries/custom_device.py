#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  @file       custom_device.py
  @brief      噪音分贝转换库Python版
  @copyright  Copyright (c) 2025 Your Name
  @license    The MIT License (MIT)
  @author     Your Name
  @version    V1.0.0
  @date       2025-05-16
  
  使用说明:
  1. 将此文件复制到Mind+扩展的python/libraries目录中
  2. 在代码中使用 from custom_device import CustomDevice
  3. 创建设备对象: device = CustomDevice()
  4. 使用方法:
     - device.begin() - 初始化设备
     - device.read_raw_data() - 读取原始数据
     - device.read_processed_data() - 读取处理后数据
     - device.read_status_value() - 读取状态值
     - device.set_parameter(value) - 设置参数值
     - device.perform_action() - 执行动作
'''

import time
import random
import sys
import os

# 设备常量定义
DEVICE_ADDR = 0x23      # 官方指定I2C地址
REG_ID = 0x00           # 设备ID寄存器地址
REG_RAW_DATA = 0x06     # 原始数据寄存器
REG_PROCESSED = 0x07    # 处理后数据寄存器
REG_STATUS = 0x08       # 状态寄存器
DEVICE_ID = 0x427c      # 原始设备ID
DEVICE_ID_REV = 0x7c42  # 字节序颠倒的设备ID

# 全局变量
PINPONG_AVAILABLE = False

# 尝试导入PinPong库（适用于行空板）
try:
    from pinpong.board import I2C, Board
    # 初始化行空板Board对象
    board = Board("unihiker")
    board.begin()
    PINPONG_AVAILABLE = True
    print("PinPong库导入成功")
except ImportError:
    # 尝试其他可能路径
    try:
        # 行空板可能的路径
        paths = [
            "/usr/lib/python3/dist-packages",
            "/usr/local/lib/python3/dist-packages",
            os.path.expanduser("~/.local/lib/python3/dist-packages"),
            "/usr/share/unihiker/lib"
        ]
        
        # 添加路径
        for path in paths:
            if path not in sys.path and os.path.exists(path):
                sys.path.append(path)
        
        # 再次尝试导入
        from pinpong.board import I2C, Board
        board = Board("unihiker")
        board.begin()
        PINPONG_AVAILABLE = True
        print("PinPong库导入成功（第二次尝试）")
    except ImportError as e:
        print(f"警告: 无法导入PinPong库: {e}")
        print("将尝试使用smbus库")
        PINPONG_AVAILABLE = False

# 如果PinPong不可用，尝试使用smbus
if not PINPONG_AVAILABLE:
    try:
        import smbus
        print("使用smbus库")
    except ImportError:
        print("警告: 无法导入smbus库，将使用模拟数据")


class CustomDevice:
    """自定义设备类，支持行空板和普通Python环境"""
    
    def __init__(self, bus_num=1, address=DEVICE_ADDR, force_real=False):
        """初始化设备对象
        
        Args:
            bus_num: I2C总线号，默认为1
            address: 设备地址，默认0x23
            force_real: 是否强制使用真实设备，不允许模拟
        """
        self._address = address
        self._initialized = False
        self._force_real = force_real
        self._simulate = False
        
        # 检测是否在行空板环境
        if PINPONG_AVAILABLE:
            self._i2c = I2C(bus_num)
            self._use_pinpong = True
        else:
            try:
                self._i2c = smbus.SMBus(bus_num)
                self._use_pinpong = False
            except:
                if force_real:
                    raise RuntimeError("无法初始化硬件总线，且不允许模拟")
                self._simulate = True
                print("警告: 无法初始化硬件总线，将使用模拟数据")
        
    def begin(self):
        """初始化设备
        
        Returns:
            bool: 初始化是否成功
        """
        # 如果使用模拟数据，直接返回成功
        if self._simulate:
            self._initialized = True
            return True
            
        try:
            # 读取设备ID确认设备存在
            device_id = self._read_register_word(REG_ID)
            
            # 检查设备ID是否匹配（考虑字节序）
            if device_id != DEVICE_ID and device_id != DEVICE_ID_REV:
                if self._force_real:
                    return False
                
                # 如果设备ID不匹配，但允许模拟，则使用模拟模式
                print(f"设备ID不匹配: 获取{device_id:04x}, 期望{DEVICE_ID:04x}, 使用模拟模式")
                self._simulate = True
            
            self._initialized = True
            return True
        except Exception as e:
            if self._force_real:
                print(f"初始化设备失败: {e}")
                return False
            
            # 出现异常但不强制使用真实设备，使用模拟模式
            print(f"初始化设备失败: {e}, 使用模拟模式")
            self._simulate = True
            self._initialized = True
            return True
    
    def read_raw_data(self):
        """读取原始数据
        
        Returns:
            int: 原始数据值
        """
        if not self._initialized and not self.begin():
            return 0
            
        if self._simulate:
            # 生成随机模拟数据
            return random.randint(0, 1024)
        
        try:
            return self._read_register_word(REG_RAW_DATA)
        except Exception as e:
            print(f"读取原始数据失败: {e}")
            return 0
    
    def read_processed_data(self):
        """读取处理后数据
        
        Returns:
            int: 处理后的数据值
        """
        if not self._initialized and not self.begin():
            return 0
            
        if self._simulate:
            # 模拟数据处理
            raw = random.randint(0, 1024)
            return int(raw / 100)
        
        try:
            return self._read_register_word(REG_PROCESSED)
        except Exception as e:
            print(f"读取处理后数据失败: {e}")
            return 0
    
    def read_status_value(self):
        """读取状态值
        
        Returns:
            int: 状态值
        """
        if not self._initialized and not self.begin():
            return 0
            
        if self._simulate:
            # 模拟状态值 (0-5)
            return random.randint(0, 5)
        
        try:
            return self._read_register_word(REG_STATUS) & 0xFF
        except Exception as e:
            print(f"读取状态值失败: {e}")
            return 0
    
    def set_parameter(self, value):
        """设置参数值
        
        Args:
            value: 参数值 (0-100)
        """
        if not self._initialized and not self.begin():
            return
            
        # 确保参数在合理范围内
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
            
        if self._simulate:
            # 模拟模式下不做任何操作
            return
        
        try:
            # 写入参数到寄存器
            self._write_register_word(0x10, value)
        except Exception as e:
            print(f"设置参数失败: {e}")
    
    def perform_action(self):
        """执行设备动作"""
        if not self._initialized and not self.begin():
            return
            
        if self._simulate:
            # 模拟模式下不做任何操作
            return
        
        try:
            # 写入命令触发设备动作
            self._write_register_word(0x20, 0x01)
        except Exception as e:
            print(f"执行动作失败: {e}")
    
    def _read_register_word(self, register):
        """从寄存器读取2字节数据
        
        Args:
            register: 寄存器地址
            
        Returns:
            int: 读取的16位数据
        """
        if self._use_pinpong:
            # 行空板PinPong库方式读取
            value = self._i2c.readfrom_mem(self._address, register, 2)
            return value[0] | (value[1] << 8)
        else:
            # SMBus方式读取
            low = self._i2c.read_byte_data(self._address, register)
            high = self._i2c.read_byte_data(self._address, register + 1)
            return low | (high << 8)
    
    def _write_register_word(self, register, value):
        """向寄存器写入2字节数据
        
        Args:
            register: 寄存器地址
            value: 要写入的16位数据
        """
        if self._use_pinpong:
            # 行空板PinPong库方式写入
            data = [value & 0xFF, (value >> 8) & 0xFF]
            self._i2c.writeto_mem(self._address, register, data)
        else:
            # SMBus方式写入
            self._i2c.write_byte_data(self._address, register, value & 0xFF)
            self._i2c.write_byte_data(self._address, register + 1, (value >> 8) & 0xFF)


# 简单测试代码
if __name__ == "__main__":
    print("自定义设备库测试")
    
    device = CustomDevice()
    if device.begin():
        print("设备初始化成功")
        
        try:
            while True:
                raw_data = device.read_raw_data()
                processed = device.read_processed_data()
                status = device.read_status_value()
                
                print(f"原始数据: {raw_data}")
                print(f"处理后数据: {processed}")
                print(f"状态值: {status}")
                print("-" * 20)
                
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n程序已停止")
    else:
        print("设备初始化失败")