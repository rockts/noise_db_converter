#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  @file       noise_converter.py
  @brief      噪音分贝转换库Python版
  @copyright  Copyright (c) 2025 Your Name
  @license    The MIT License (MIT)
  @author     Your Name
  @version    V1.0.0
  @date       2025-05-16
  
  使用说明:
  1. 将此文件复制到Mind+扩展的python/libraries目录中
  2. 在代码中使用 from noise_converter import convert_to_decibel
  3. 使用方法: db = convert_to_decibel(adc_value)
'''

import math

def convert_to_decibel(adc_value):
    """将模拟值转换为分贝(dB)值
    
    使用公式: voltage = adc_value / 4095 * 3.3
             dB = 20 * log10((voltage + 0.001) / 0.00631)
    
    Args:
        adc_value: 模拟值 (0-4095)
        
    Returns:
        float: 分贝值 (dB)
    """
    try:
        # 确保输入值是数字
        adc_value = float(adc_value)
        
        # 打印调试信息
        print(f"DEBUG: 正在处理ADC值: {adc_value}")
        
        # 将ADC值转换为电压值
        voltage = adc_value / 4095.0 * 3.3
        print(f"DEBUG: 计算得到电压值: {voltage:.6f}V")
        
        # 然后计算分贝，加0.001防止log10(0)
        decibel = 20.0 * math.log10((voltage + 0.001) / 0.00631)
        print(f"DEBUG: 转换后的分贝值: {decibel:.2f}dB")
        
        return decibel
    except Exception as e:
        print(f"转换分贝值出错: {e}")
        return 0.0

# 简单测试
if __name__ == "__main__":
    test_values = [0, 1000, 2048, 3000, 4095]
    for val in test_values:
        db = convert_to_decibel(val)
        print(f"ADC值: {val}, 分贝值: {db:.2f} dB")
