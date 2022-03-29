帝国cms目录遍历脚本



**Author·:Air**



**`写了一堆bug`**



食用方法

```
git clone git@github.com:SkinAir/Empirecmscan.git
cd /Empirecmscan
python3 CMScan.py -h
python3 CMScan.py -u https://1xxxx
```

#EmpireDir为Empirecms7.2版本

------

若使用其他cms，则使用`dir.py`遍历本地目录

```
python3 dir.py
```

#`dir.py`遍历所需cms的本地路径







| **帝国CMS目录结构介绍**                                      |
| ------------------------------------------------------------ |
| **/ 系统根目录**<br/>├d/       附件和数据存放目录 (data)<br/>│├file/    附件存放目录<br/>│├js/     JS调用生成目录<br/>│└txt/     内容存文本存放目录<br/>├e/       系统程序目录 (empire)<br/>├html/     自定义内容页存放预设目录<br/>├images/    默认模板图片目录<br/>├s/       专题目录 (special)<br/>├search/    高级搜索页面目录<br/>├skin/     模板CSS和图片存放目录<br/>├testdata/   内置测试数据的附件目录 (安装时选择测试数据用的，不内置测试数据可以删除)<br/>└index.html   网站首页<br /><br />**/e/ 系统程序目录**<br/>├action/    信息动态列表页和内容页目录<br/>├admin/     后台目录 (可重命名)<br/>├class/     系统核心文件目录<br/>├data/     系统处理数据相关目录 (临时文件、缓存等)<br/>├DoInfo/    前台会员管理信息目录 (页面模板e/template/DoInfo)<br/>├DoPrint/    打印页面目录<br/>├DownSys/    下载系统模型功能目录 (页面模板e/template/DownSys)<br/>├enews/     前台处理数据入口文件<br/>├extend/    扩展程序目录<br/>├ftp/      FTP识别目录<br/>├install/    安装程序目录，安装后请删除掉<br/>├member/    前台会员功能目录 (页面模板e/template/member)<br/>├message/    提示信息页面目录<br/>├NewsSys/    新闻系统模型功能目录<br/>├payapi/    在线支付接口目录 (页面模板e/template/payapi)<br/>├pl/      评论页目录<br/>├public/    公用功能程序目录 (页面模板e/template/public)<br/>├sch/      全站全文搜索生成目录<br/>├search/    普通搜索文件目录<br/>├ShopSys/    商城系统模型功能目录 (页面模板e/template/ShopSys)<br/>├ShowKey/    前台验证码文件目录<br/>├space/     会员空间目录 (其中template为会员空间模板目录)<br/>├tags/     TAGS列表文件目录<br/>├tasks/     计划任务脚本存放目录<br/>├template/   前台动态页的模板目录<br/>├tool/     插件相关功能目录 (页面模板e/template/tool)<br/>├update/    升级程序目录 (升级程序复制到这个目录运行)<br/>├ViewImg/    显示图片大图目录<br/>├wap/      WAP功能目录 (其中template为WAP模板目录)<br/>└web/      RSS显示文件目录<br /><br />**/e/template/ 动态页面模板目录**<br/>├DoInfo/         前台投稿模板目录 (对应程序目录：/e/DoInfo/)<br/>│├AddInfo.php      发布投稿页面模板 (对应程序文件：/e/DoInfo/AddInfo.php)<br/>│├ChangeClass.php    发布投稿选择栏目页面模板 (对应程序文件：/e/DoInfo/ChangeClass.php)<br/>│├DoInfo.php       管理投稿首页页面模板 (对应程序文件：/e/DoInfo/index.php)<br/>│└tran.php        发布投稿上传附件页面模板 (对应程序文件：/e/DoInfo/tran.php)<br/>├DownSys/         下载模型页面模板目录 (对应程序目录：/e/DownSys/)<br/>│└report.php       提交错误报告页面模板 (对应程序文件：/e/report/index.php)<br/>├member/         会员中心模板目录 (对应程序目录：/e/member/)<br/>│├memberlist/      会员列表页面模板目录 (对应程序文件：/e/member/list/index.php)<br/>│├mspace/        管理会员空间页面模板目录 (对应程序目录：/e/member/mspace/)<br/>││├ChangeStyle.php   选择空间模板页面模板 (对应程序文件：/e/member/mspace/ChangeStyle.php)<br/>││├feedback.php     管理会员空间反馈页面模板 (对应程序文件：/e/member/mspace/feedback.php)<br/>││├gbook.php      管理会员空间留言页面模板 (对应程序文件：/e/member/mspace/gbook.php)<br/>││├ReGbook.php     管理会员空间留言回复页面模板 (对应程序文件：/e/member/mspace/ReGbook.php)<br/>││├SetSpace.php     设置会员空间页面模板 (对应程序文件：/e/member/mspace/SetSpace.php)<br/>││└ShowFeedback.php   管理会员空间反馈显示反馈页面模板 (对应程序文件：/e/member/mspace/ShowFeedback.php)<br/>│├AddFava.php      增加收藏页面模板 (对应程序文件：/e/member/fava/add/index.php)<br/>│├AddFriend.php     增加好友页面模板 (对应程序文件：/e/member/friend/add/index.php)<br/>│├AddMsg.php       发送站内信息页面模板 (对应程序文件：/e/member/msg/AddMsg/index.php)<br/>│├buybak.php       购买记录页面模板 (对应程序文件：/e/member/buybak/index.php)<br/>│├buygroup.php      购买充值类型页面模板 (对应程序文件：/e/member/buygroup/index.php)<br/>│├card.php        点卡充值页面模板 (对应程序文件：/e/member/card/index.php)<br/>│├ChangeFriend.php    选择好友页面模板 (对应程序文件：/e/member/friend/FriendClass/index.php)<br/>│├ChangeRegister.php   选择注册会员组页面模板 (对应程序文件：/e/member/register/ChangeRegister.php)<br/>│├cp.php         会员中心首页页面模板 (对应程序文件：/e/member/cp/index.php)<br/>│├downbak.php      消费记录页面模板 (对应程序文件：/e/member/downbak/index.php)<br/>│├EditInfo.php      修改资料页面模板 (对应程序文件：/e/member/EditInfo/index.php)<br/>│├EditSafeInfo.php    修改安全资料页面模板 (对应程序文件：/e/member/EditInfo/EditSafeInfo.php)<br/>│├fava.php        管理收藏页面模板 (对应程序文件：/e/member/fava/index.php)<br/>│├FavaClass.php     管理收藏分类页面模板 (对应程序文件：/e/member/fava/FavaClass/index.php)<br/>│├friend.php       管理好友页面模板 (对应程序文件：/e/member/friend/index.php)<br/>│├FriendClass.php    管理好友分类页面模板 (对应程序文件：/e/member/friend/FriendClass/index.php)<br/>│├getpass.php      取回密码重置页面模板 (对应程序文件：/e/member/GetPassword/getpass.php)<br/>│├GetPassword.php    取回密码页面模板 (对应程序文件：/e/member/GetPassword/index.php)<br/>│├login.php       会员登录页面模板 (对应程序文件：/e/member/login/index.php)<br/>│├loginopen.php     弹出页面提示重新登陆页面模板 (对应程序文件：/e/member/login/login.php)<br/>│├msg.php        管理站内信息页面模板 (对应程序文件：/e/member/msg/index.php)<br/>│├my.php         我的状态页面模板 (对应程序文件：/e/member/my/index.php)<br/>│├register.php      会员注册页面模板 (对应程序文件：/e/member/register/index.php)<br/>│├regsend.php      注册激活帐号页面模板 (对应程序文件：/e/member/register/regsend.php)<br/>│├ShowInfo.php      查看会员资料页面模板 (对应程序文件：/e/member/ShowInfo/index.php)<br/>│└ViewMsg.php      查看站内信息内容页面模板 (对应程序文件：/e/member/msg/ViewMsg/index.php)<br/>├payapi/         在线支付页面模板目录 (对应程序目录：/e/payapi/)<br/>│└payapi.php       在线支付页面模板 (对应程序文件：/e/payapi/index.php)<br/>├public/         公共程序页面模板目录 (对应程序目录：/e/public/)<br/>│└vote.php        信息投票结果页面模板 (对应程序文件：/e/public/vote/index.php)<br/>├ShopSys/         商城模型页面模板目录 (对应程序目录：/e/ShopSys/)<br/>│├buycar.php       购物车页面模板 (对应程序文件：/e/ShopSys/buycar/index.php)<br/>│├ListDd.php       管理商城订单页面模板 (对应程序文件：/e/ShopSys/ListDd/index.php)<br/>│├order.php       订单提交表单页面模板 (对应程序文件：/e/ShopSys/order/index.php)<br/>│├ShowDd.php       查看商城订单内容页面模板 (对应程序文件：/e/ShopSys/ShowDd/index.php)<br/>│└SubmitOrder.php    订单提交最终确认页面模板 (对应程序文件：/e/ShopSys/SubmitOrder/index.php)<br/>└tool/          内置插件模板目录 (对应程序目录：/e/tool/)<br/> └vote.php       投票插件结果页面模板 (对应程序文件：/e/tool/vote/index.php)<br /> |

目录结构来自：`墨鱼`





