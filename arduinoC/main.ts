// 主命名空间 - 使用与噪音相关的颜色和图标
//% color="#FF5722" icon="\uf130" block="噪音分贝转换"
//% version="1.0.0"
namespace noiseDbConverter {    /**
     * 将模拟值转换为分贝(dBA)值
     * 使用DFRobot SEN0232标准公式: 分贝值(dBA) = 输出电压(V) × 50
     * 当输出电压为0.6V时，分贝值为30dBA
     * 当输出电压为2.6V时，分贝值为130dBA
     * @param adcValue 模拟值 (0-4095)
     */
    //% block="将模拟值 [adcValue] 转换为分贝"
    //% adcValue.shadow="number" adcValue.defl=2048
    //% blockType="reporter"
    //% weight=100
    export function convertToDecibel(parameter: any, block: any): void {
        let adcValue = parameter.adcValue.code;

        // 生成转换代码 - 使用DFRobot标准公式，并限制在测量范围内
        Generator.addCode(`(constrain((${adcValue} / 4095.0 * 3.3 * 50.0), 30.0, 130.0))`);
    }
}
