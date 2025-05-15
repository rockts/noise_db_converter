# Mind+ 自定义积木模板

这是一个用于 Mind+的自定义积木模板，支持 Arduino Uno 和行空板（Unihiker）。使用本模板可以快速创建和管理自定义积木，适用于各种教学和开发需求。

## 模板特点

- 🌟 双平台支持：同时支持 Arduino 和行空板平台
- 🧩 积木化编程：提供直观的积木块，易于使用
- 🛠️ 完整源码：包含 C++和 Python 双语言实现
- 📚 中英文支持：完整的双语翻译
- 🔌 错误处理：健壮的设备连接和通信错误处理
- 🔄 模拟模式：无硬件时可使用模拟数据进行开发测试

## 目录结构

```
/
├── config.json               # 扩展配置文件
├── LICENSE                   # MIT许可证
├── README.md                 # 中文文档
├── README_EN.md              # 英文文档
├── examples.md               # 使用示例
├── package.sh                # 打包脚本
├── arduinoC/                 # Arduino平台相关文件
│   ├── main.ts               # Arduino积木定义
│   ├── _images/              # 积木图标和图片
│   │   ├── readme.md
│   │   └── icons/
│   ├── _locales/             # 多语言支持
│   │   ├── en.json           # 英文语言包
│   │   └── zh-cn.json        # 中文语言包
│   └── libraries/            # Arduino库文件
│       ├── CustomDevice.h    # 设备库头文件
│       ├── CustomDevice.cpp  # 设备库实现
│       └── libraries.zip     # 打包库文件
└── python/                   # Python平台相关文件
    ├── main.ts               # Python积木定义
    ├── _images/              # 积木图标和图片
    │   ├── readme.md
    │   └── icons/
    ├── _locales/             # 多语言支持
    │   ├── en.json           # 英文语言包
    │   └── zh-cn.json        # 中文语言包
    └── libraries/            # Python库文件
        ├── custom_device.py  # Python设备库
        └── libraries.zip     # 打包库文件
```

## 积木功能

模板默认提供以下积木功能：

1. **初始化设备** - 初始化硬件连接
2. **读取数据** - 支持读取原始数据、处理后数据和状态值
3. **设置参数** - 允许设置 0-100 范围内的参数值
4. **执行动作** - 触发设备执行特定操作

## 使用方法

### 1. 创建自己的积木扩展

1. 复制此模板文件夹作为起点
2. 修改`config.json`中的配置信息，包括名称、作者等
3. 根据需要修改`main.ts`文件中的积木定义
4. 根据硬件需求修改`CustomDevice.h`/`CustomDevice.cpp`或`custom_device.py`

### 2. Arduino 库开发指南

Arduino 库使用 C++开发，位于`arduinoC/libraries/`目录下：

- 修改`CustomDevice.h`中的常量定义（如设备地址、寄存器地址）
- 在`CustomDevice.cpp`中实现各功能的具体逻辑
- 添加新方法时，记得同时更新头文件和实现文件
- 使用`ENABLE_DBG`宏控制调试信息输出

### 3. Python 库开发指南

Python 库位于`python/libraries/`目录下：

- `custom_device.py`包含完整的行空板支持代码
- 默认支持 PinPong 库（行空板专用）和 smbus 库（标准 I2C）
- 提供模拟模式，当硬件不可用时自动切换
- 添加新功能时，需要更新相应的读写方法

### 4. 积木定义指南

积木在 TypeScript 文件中定义：

- 使用 Pxt 风格的装饰器定义积木
- 可在`blockType`中设置积木类型：`"command"`或`"reporter"`
- 使用`weight`参数控制积木显示顺序
- 可添加自定义参数，如下拉菜单、数值范围等

### 5. 打包发布

完成开发后，使用`package.sh`脚本打包扩展：

```bash
./package.sh
```

生成的`.mpext`文件可直接在 Mind+中导入使用。

## 支持的硬件

- Arduino Uno（通过 I2C 通信）
- 行空板 Unihiker（通过 PinPong 库）

## 定制指南

请参阅各文件中的注释了解如何自定义积木功能和外观。更多高级定制请参考[Mind+文档](https://mindplus.dfrobot.com.cn/extensions-guide)。

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件。

## 作者

您的名字 (your.email@example.com)

---

欢迎贡献代码，提交问题或改进建议！
