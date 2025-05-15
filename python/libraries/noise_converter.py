#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  @file       noise_converter.py
  @brief      噪音分贝转换库Python版
  @copyright  Copyright (c) 2025 rockts
  @license    The MIT License (MIT)
  @author     rockts (gaopeng@lekee.cc)
  @version    V1.0.0
  @date       2025-05-16
  
  使用说明:
  1. 将此文件复制到Mind+扩展的python/libraries目录中
  2. 在代码中使用 from noise_converter import convert_to_decibel
  3. 使用方法: dba = convert_to_decibel(adc_value)
'''

import math

def convert_to_decibel(adc_value):
    """将模拟值转换为分贝(dB)值
    
    使用DFRobot SEN0232标准公式: 分贝值(dBA) = 输出电压(V) × 50
    当输出电压为0.6V时，分贝值为30dBA
    当输出电压为2.6V时，分贝值为130dBA
    
    Args:
        adc_value: 模拟值 (0-4095)
        
    Returns:
        float: 分贝值 (dBA)
    """
    try:
        # 确保输入值是数字
        adc_value = float(adc_value)
        
        # 将ADC值转换为电压值
        voltage = adc_value / 4095.0 * 3.3
        
        # 根据DFRobot SEN0232标准公式计算分贝值
        decibel = voltage * 50.0
        
        # 限制在传感器的测量范围内（30dBA~130dBA）
        if decibel < 30.0:
            decibel = 30.0
        elif decibel > 130.0:
            decibel = 130.0
            
        return decibel
    except Exception as e:
        print(f"转换分贝值出错: {e}")
        return 0.0

# 简单测试
if __name__ == "__main__":
    test_values = [0, 1000, 2048, 3000, 4095]
    print("ADC值 -> 分贝值(dBA):")
    for val in test_values:
        voltage = val / 4095.0 * 3.3
        db = convert_to_decibel(val)
        print(f"{val:4d} -> {db:.2f} dBA (电压: {voltage:.2f}V)")
