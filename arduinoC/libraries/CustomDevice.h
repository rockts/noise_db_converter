/**
 * @file CustomDevice.h
 * @brief 自定义设备库的头文件
 * @copyright Copyright (c) 2025 Your Name
 * @license The MIT License (MIT)
 * @author [Your Name](your.email@example.com)
 * @version V1.0.0
 * @date 2025-05-16
 */

#ifndef CUSTOM_DEVICE_H
#define CUSTOM_DEVICE_H

#include <Arduino.h>
#include <Wire.h>

// 设备常量定义
#define DEVICE_ADDR 0x23   // I2C设备地址
#define REG_RAW_DATA 0x06  // 原始数据寄存器
#define REG_PROCESSED 0x07 // 处理后数据寄存器
#define REG_STATUS 0x08    // 状态寄存器
#define DEVICE_ID 0x427c   // 设备ID

// 调试开关，取消注释可开启详细调试信息
// #define ENABLE_DBG
#ifdef ENABLE_DBG
#define DBG(...)                     \
    {                                \
        Serial.print("[");           \
        Serial.print(__FUNCTION__);  \
        Serial.print("(): ");        \
        Serial.print(__LINE__);      \
        Serial.print(" ] ");         \
        Serial.println(__VA_ARGS__); \
    }
#else
#define DBG(...)
#endif

/**
 * @brief 自定义设备类
 * @details 封装了与自定义设备的通信和数据处理功能
 */
class CustomDevice
{
public:
    /**
     * @brief 构造函数，I2C接口
     * @param pWire I2C总线指针
     */
    CustomDevice(TwoWire *pWire = &Wire);

    /**
     * @brief 初始化设备
     * @return 是否成功初始化
     */
    bool begin(void);

    /**
     * @brief 读取原始数据
     * @return 原始数据值
     */
    uint16_t readRawData(void);

    /**
     * @brief 读取处理后数据
     * @return 处理后的数据值
     */
    uint16_t readProcessedData(void);

    /**
     * @brief 读取状态值
     * @return 设备状态值
     */
    uint8_t readStatusValue(void);

    /**
     * @brief 设置设备参数
     * @param value 参数值 (0-100)
     */
    void setParameter(uint8_t value);

    /**
     * @brief 执行设备动作
     */
    void performAction(void);

private:
    TwoWire *_wire;
    uint8_t _addr = DEVICE_ADDR;
    bool _initialized = false;

    /**
     * @brief 从I2C寄存器读取数据
     * @param reg 寄存器地址
     * @return 读取的数据
     */
    uint16_t readRegister(uint8_t reg);

    /**
     * @brief 向I2C寄存器写入数据
     * @param reg 寄存器地址
     * @param val 要写入的数据
     * @return 是否写入成功
     */
    bool writeRegister(uint8_t reg, uint16_t val);
};

#endif // CUSTOM_DEVICE_H
