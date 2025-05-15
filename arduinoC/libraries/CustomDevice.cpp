/**
 * @file CustomDevice.cpp
 * @brief 自定义设备库的实现文件
 * @copyright Copyright (c) 2025 Your Name
 * @license The MIT License (MIT)
 * @author [Your Name](your.email@example.com)
 * @version V1.0.0
 * @date 2025-05-16
 */

#include "CustomDevice.h"

/**
 * 构造函数，初始化I2C总线
 */
CustomDevice::CustomDevice(TwoWire *pWire)
{
    _wire = pWire;
}

/**
 * 初始化设备
 */
bool CustomDevice::begin(void)
{
    // 检查设备是否存在，可通过读取设备ID确认
    delay(10); // 给设备上电时间

    _wire->begin();

    // 尝试读取设备ID
    _wire->beginTransmission(_addr);
    _wire->write(0x00); // 设备ID寄存器
    if (_wire->endTransmission() != 0)
    {
        DBG("Device not found");
        return false;
    }

    _wire->requestFrom(_addr, (uint8_t)2);
    if (_wire->available() < 2)
    {
        DBG("Failed to read device ID");
        return false;
    }

    uint16_t deviceId = _wire->read();
    deviceId |= (uint16_t)_wire->read() << 8;

    if (deviceId != DEVICE_ID && deviceId != (DEVICE_ID >> 8 | DEVICE_ID << 8))
    {
        DBG("Invalid device ID");
        return false;
    }

    _initialized = true;
    DBG("Device initialized successfully");
    return true;
}

/**
 * 读取原始数据
 */
uint16_t CustomDevice::readRawData(void)
{
    if (!_initialized)
    {
        if (!begin())
        {
            return 0;
        }
    }

    return readRegister(REG_RAW_DATA);
}

/**
 * 读取处理后数据
 */
uint16_t CustomDevice::readProcessedData(void)
{
    if (!_initialized)
    {
        if (!begin())
        {
            return 0;
        }
    }

    return readRegister(REG_PROCESSED);
}

/**
 * 读取状态值
 */
uint8_t CustomDevice::readStatusValue(void)
{
    if (!_initialized)
    {
        if (!begin())
        {
            return 0;
        }
    }

    uint16_t val = readRegister(REG_STATUS);
    return (uint8_t)(val & 0xFF);
}

/**
 * 设置设备参数
 */
void CustomDevice::setParameter(uint8_t value)
{
    if (!_initialized)
    {
        if (!begin())
        {
            return;
        }
    }

    // 限制参数范围
    if (value > 100)
        value = 100;

    // 写入参数到设备
    writeRegister(0x10, value);
}

/**
 * 执行设备动作
 */
void CustomDevice::performAction(void)
{
    if (!_initialized)
    {
        if (!begin())
        {
            return;
        }
    }

    // 写入命令触发设备动作
    writeRegister(0x20, 0x01);
}

/**
 * 从I2C寄存器读取数据（私有方法）
 */
uint16_t CustomDevice::readRegister(uint8_t reg)
{
    _wire->beginTransmission(_addr);
    _wire->write(reg);
    if (_wire->endTransmission() != 0)
    {
        DBG("Failed to set register address");
        return 0;
    }

    _wire->requestFrom(_addr, (uint8_t)2);
    if (_wire->available() < 2)
    {
        DBG("Failed to read from register");
        return 0;
    }

    uint16_t value = _wire->read();
    value |= (uint16_t)_wire->read() << 8;

    return value;
}

/**
 * 向I2C寄存器写入数据（私有方法）
 */
bool CustomDevice::writeRegister(uint8_t reg, uint16_t val)
{
    _wire->beginTransmission(_addr);
    _wire->write(reg);
    _wire->write(val & 0xFF);
    _wire->write((val >> 8) & 0xFF);
    if (_wire->endTransmission() != 0)
    {
        DBG("Failed to write to register");
        return false;
    }

    return true;
}
