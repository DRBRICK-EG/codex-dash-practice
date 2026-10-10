# DR.BRICK · 3 秒口号片头

口号：**دكتور بريك… فرحة بإيدك!**  
中文意译：**DR.BRICK，快乐亲手拼！**

- [直接打开 MP4](https://raw.githubusercontent.com/DRBRICK-EG/codex-dash-practice/drbrick-brand-character/brand-assets/slogan-intro/drbrick-slogan-intro-3s.mp4)
- [独立人声 WAV](https://raw.githubusercontent.com/DRBRICK-EG/codex-dash-practice/drbrick-brand-character/brand-assets/slogan-intro/drbrick-slogan-voice.wav)
- [预览图](preview.jpg)

采用已有无胡子卡通品牌人物和原版透明背景 logo。人物轻微摆动，嘴部随人声音量开合，字幕分句出现，配以轻微提示音。属于二维人物动画；嘴部动作由音量驱动，并非逐音素口型匹配。

声音为本地 Piper / Sherpa-ONNX `ar_JO-kareem-medium` 阿拉伯语合成男声，不是本人声线克隆，也未模拟本人的声音。模型语言标签为约旦阿拉伯语；不将其标注为经母语者审校的埃及口音录音。

输出：1080 × 1920，9:16，3.000 秒，30 fps；H.264 Constrained Baseline，yuv420p；AAC-LC，48 kHz 双声道；MP4 faststart。独立 WAV 为不带提示音的人声，可用于后续剪辑。

把 MP4 放在后续产品视频的最前面即可；本片头没有绑定某一款具体产品。

语音模型来源：https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models  
模型卡指向的训练数据：https://github.com/AliMokhammad/arabicttstrain/

验证结果：全片解码无报错；Chromium 浏览器起播、跳转和播放至结尾正常。未在实体 Windows 设备上实测。
