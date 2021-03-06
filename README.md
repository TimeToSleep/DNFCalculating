# DNFCalculating

主要框架由纸飞机实现，西瓜协助修改，SCUDRT 优化排序，python 编写，pyqt5 图形 GUI 库<br>
<b>如果有兴趣添加职业整合,可加群：1019815121,记得备注下职业</b><br>
执行程序下载:https://lanzous.com/b01bfj76f

## 各职业实现

女大枪(纸飞机提供)、男大枪(幕城提供)、剑魔(爱敏 777 提供)由纸飞机完成<br>
狂战士(爱敏提供) 剑豪(爱敏提供) 光枪(爱敏提供) 毒王(雅男提供)由纸飞机完成<br>
女机械由荔枝贝壳完成<br>
女弹药由西瓜完成<br>
将军由 RBQ 小一完成<br>
冰洁由平静完成<br>
元素圣灵由碳末完成(平静协助)<br>
剑影由亚索完成<br>
男漫游由 Garson 完成<br>
审判由 Paxis 完成<br>
特工由碳末完成<br>

## 程序目录结构说明

### Part 目录

职业相关文件目录,由职业名.py 及 sum.py 组成,职业名.py 负责各个职业的个性化数据,sum.py 负责引用所有职业<br>
若项目文件打开时图片显示不正常请将 pyqt5 版本更新至 5.14.2 或以上<br>

### ResourceFiles 目录

资源文件目录,由公用资源文件及职业资源文件组成<br>

### main.py

程序入口页面,职业相关部分已经抽出,无需修改<br>

### PublicReference 目录

公共实现部分,由 base.py 装备.py 装备函数.py 组成

#### PublicReference/base.py

核心算法及主体界面绘制部分<br>
常规无需修改该部分,如需要优化程序的效率及部分算法，可尝试修改<br>
主体核心可优化空间比较大,但由于接触 PY 才几个礼拜,对 PY 多核心运算的不熟悉,暂不打算修改,欢迎尝试优化

#### PublicReference/装备.py

装备及套装数据部分<br>
如需要添加修改装备.可在此处修改,注意装备的后缀数字,需要与 img/装备下的文件名一致(新增需要同步添加图标)

#### PublicReference/装备函数.py

一些计算公式部分,除非公式出现偏差,否则无需修改<br>

## 添加一个职业的步骤

1 - 在 Part 目录下,创建职业.py 文件,实现参考其他职业,<br>
2 - 在 ResourceFiles 目录下创建对应的职业素材文件夹,结构参考其他职业<br>
3 - 在技能文件夹中添加技能图标,图片后缀为 png,buff 图标命名为 BUFF.png<br>
4 - 参考其他职业,在.py 文件中完善技能数据及部分特殊的算法(如果有比较奇怪的算法需要时间,可以参考芙蕾雅.py)<br>
5 - 在 Part/sum.py 中引入并添加对应职业<br>

## 其余说明

由于技能及被动等已经做过抽象化同时进行过扩展,因此大部分职业只需要录入基础数据等就可以<br>
小部分采用/CD 无法计算的续航类技能等,可参考芙蕾雅.py 进行计算函数个性化实现<br>
技能及被动等只扩展了技能的三条属性,第一条技能 hit 默认 1,2|3 条 hit 默认为 0,需要手动赋值<br>
如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数<br>
固伤在填写基础及成长的时候需要注意,技能面板/独立得到的成长及数值需要\*100<br>
如果需要添加武器,在 PublicReference/装备.py 添加装备属性,同时在 ResourceFiles/img/装备装备下添加对应图标

# 更新日志

## 2020.5.26

新增刹那永恒 By 平静<br>
修复排序 BUG(低于第一组伤害的组合不显示)

## 2020.5.27

删除整理狂战/剑豪/毒王/光枪数据<br>

## 2020.5.27

狂战士(爱敏提供) 剑豪(爱敏提供) 光枪(爱敏提供) 毒王(雅男提供) 技能数据重新录入<br>
新增元素圣灵 Byww

## 2020.5.29

新增剑影 By 亚索<br>
新增男漫游 By Garson<br>
新增审判 By Paxis<br>

## 2020.5.30

新增特工 碳末完成<br>
新增部分 辟邪玉<br>

## 2020.5.31

新增剑宗(仅巨剑) 亚索完成(纸飞机协助)<br>
小幅度优化计算效率<br>
