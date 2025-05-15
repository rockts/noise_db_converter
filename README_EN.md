# Mind+ Custom Block Template

This is a custom block template for Mind+, supporting Arduino Uno and Unihiker. Use this template to quickly create and manage custom blocks for various teaching and development needs.

## Template Features

- 🌟 Dual Platform Support: Supports both Arduino and Unihiker platforms
- 🧩 Block Programming: Provides intuitive blocks that are easy to use
- 🛠️ Complete Source Code: Includes implementations in both C++ and Python
- 📚 Bilingual Support: Complete translations in Chinese and English
- 🔌 Error Handling: Robust device connection and communication error handling
- 🔄 Simulation Mode: Use simulated data for development and testing when hardware is unavailable

## Directory Structure

```
/
├── config.json               # Extension configuration file
├── LICENSE                   # MIT license
├── README.md                 # Chinese documentation
├── README_EN.md              # English documentation
├── examples.md               # Usage examples
├── package.sh                # Packaging script
├── arduinoC/                 # Arduino platform files
│   ├── main.ts               # Arduino block definitions
│   ├── _images/              # Block icons and images
│   │   ├── readme.md
│   │   └── icons/
│   ├── _locales/             # Multilingual support
│   │   ├── en.json           # English language pack
│   │   └── zh-cn.json        # Chinese language pack
│   └── libraries/            # Arduino libraries
│       ├── CustomDevice.h    # Device library header
│       ├── CustomDevice.cpp  # Device library implementation
│       └── libraries.zip     # Packaged library files
└── python/                   # Python platform files
    ├── main.ts               # Python block definitions
    ├── _images/              # Block icons and images
    │   ├── readme.md
    │   └── icons/
    ├── _locales/             # Multilingual support
    │   ├── en.json           # English language pack
    │   └── zh-cn.json        # Chinese language pack
    └── libraries/            # Python libraries
        ├── custom_device.py  # Python device library
        └── libraries.zip     # Packaged library files
```

## Block Features

The template provides the following block features by default:

1. **Initialize Device** - Initialize hardware connection
2. **Read Data** - Support for reading raw data, processed data, and status values
3. **Set Parameter** - Allow setting parameter values in the 0-100 range
4. **Perform Action** - Trigger the device to perform a specific operation

## Usage Guide

### 1. Creating Your Own Block Extension

1. Copy this template folder as a starting point
2. Modify the configuration in `config.json`, including name, author, etc.
3. Modify the block definitions in `main.ts` files as needed
4. Modify `CustomDevice.h`/`CustomDevice.cpp` or `custom_device.py` according to your hardware requirements

### 2. Arduino Library Development Guide

The Arduino library is developed in C++ and located in the `arduinoC/libraries/` directory:

- Modify the constant definitions in `CustomDevice.h` (such as device address, register address)
- Implement the specific logic for each function in `CustomDevice.cpp`
- When adding new methods, remember to update both the header and implementation files
- Use the `ENABLE_DBG` macro to control debug information output

### 3. Python Library Development Guide

The Python library is located in the `python/libraries/` directory:

- `custom_device.py` contains complete Unihiker support code
- Default support for PinPong library (Unihiker-specific) and smbus library (standard I2C)
- Provides simulation mode, automatically switching when hardware is unavailable
- When adding new features, update the corresponding read/write methods

### 4. Block Definition Guide

Blocks are defined in TypeScript files:

- Use Pxt-style decorators to define blocks
- Set block types in `blockType`: `"command"` or `"reporter"`
- Use the `weight` parameter to control block display order
- Add custom parameters, such as dropdown menus, value ranges, etc.

### 5. Packaging and Publishing

After development is complete, use the `package.sh` script to package the extension:

```bash
./package.sh
```

The generated `.mpext` file can be imported directly into Mind+.

## Supported Hardware

- Arduino Uno (via I2C communication)
- Unihiker (via PinPong library)

## Customization Guide

Please refer to the comments in each file to learn how to customize block functionality and appearance. For more advanced customization, refer to the [Mind+ Documentation](https://mindplus.dfrobot.com.cn/extensions-guide).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name (your.email@example.com)

---

Contributions, issues, and feature requests are welcome!
