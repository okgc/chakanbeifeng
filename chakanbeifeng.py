# 拿页面源代码
# 提取和解析数据

import requests
import asyncio
import aiohttp
from lxml import etree
import time
import csv
import os
import re

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def hqurls():
    #获取每个标题相应的 新地址
    resp=requests.get(yurl, headers=headers)
    resp.encoding='utf-8'#指定字符集
    html=etree.HTML(resp.text)
    #拿到每一个标题的 src
    srcs=html.xpath('//*[@id="container"]/div[1]/section[4]/table/tbody/tr/td[2]/div/a/@href')
    for src in srcs:
        #进入新连接获取代码
        nresp=requests.get("https://www.jjang0u.com"+str(src), headers=headers)
        nhtml=etree.HTML(nresp.text)
        xztpsrc=nhtml.xpath('//*[@id="post_content"]/figure[1]/img/@src')
        if xztpsrc !=[]:
            urls.append(xztpsrc)
    print(urls)
    time.sleep(1)

async def aiodownload(url):
        # 通过requests.get获得图片
        r=requests.get("".join(url))
        image=r.content
        #wjm=nimg.
        # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
        with open("./jjang0u/"+"".join(url).split('/')[-1],'wb') as f:
            f.write(image)
    #s=aiohttp.ClientSession() <==> requests
    #requests.get   .post()
    #s.get()        .post()
    # async with aiohttp.ClientSession() as session: #使用with 不需要手动关闭 close
    #     async with session.get(url) as resp:
    #         with open(name,mode="wb") as f:
    #             f.write(await resp.content.read())# 读取内容是异步的，需要await  resp.text()
    #         #resp.content.read() #==> resp.content
    #     print(name,"ok")

async def main():
    tasks=[]
    for url in urls:
        d=asyncio.create_task(aiodownload(url))
        tasks.append(d)
    await asyncio.wait(tasks)
def xiazaione(newurl):
            #下载图片
        nss=session.get(newurl, headers=headers)
        nsshtml=etree.HTML(nss.text)
        tpsrcall=nsshtml.xpath('//*[@id="bo_v_con"]/img')
        for tpsrc in tpsrcall:
            xztpsrc=tpsrc.xpath('./@src')
            #判断图片有没有后续名
            if "".join(xztpsrc).find(".")>-1:
                xztpurl="".join(xztpsrc)+'.gif'
            else:
                xztpurl="".join(xztpsrc)
            xztpname=xztpurl.rsplit("/",1)[1]
            ssshtml = session.get(xztpurl)
            with open(cljs+"/"+xztpname, 'wb') as file:
                file.write(ssshtml.content)
                print("xiazai le",ssshtml)
def download_one_page(xlj,yigeid):
    resp=requests.get(xlj,headers=headers)
    scmz=namz.findall(resp.text)
    print(scmz)
    if scmz !=['카카오톡채널 - 프로필이초기화되었습니다']:
        biaoti="".join(scmz)
        dizhi="".join(yigeid)
        csvwriter.writerow([dizhi+'",'])
        resp.close() #关闭 resp

if __name__== '__main__':
    global ygjg
    global fengjg
    global nengjiajg
    ygjg=int(0)
    fengjg=int(0)
    nengjiajg=int(0)
    allid=["_xoxbTfxj","_CTTfxj","_xfKTfxj","_xiTTfxj","_kKTfxj","_QTTfxj","_ZsTfxj","_xjxbTfxj","_xmxbTfxj","_gxbTfxj","_TTTfxj","_XKTfxj","_mTTfxj","_xgTTfxj","_eKTfxj","_bxbTfxj","_IsTfxj","_nsTfxj","_exbTfxj","_xlTTfxj","_rTTfxj","_cTTfxj","_dxbTfxj","_mxbTfxj","_HxbTfxj","_dKTfxj","_xbTTfxj","_aTTfxj","_pTTfxj","_sxbTfxj","_xexbTfxj","_AKTfxj","_xbKTfxj","_xjTTfxj","_iTTfxj","_LTTfxj","_jxbTfxj","_NxbTfxj","_QxbTfxj","_xjKTfxj","_jTTfxj","_JTTfxj","_HTTfxj","_KxbTfxj","_vxbTfxj","_xgxbTfxj","_nKTfxj","_dTTfxj","_xaTTfxj","_xcTTfxj","_CxbTfxj","_WxbTfxj","_pxbTfxj","_sKTfxj","_uTTfxj","_STTfxj","_xkTTfxj","_LxbTfxj","_xbxbTfxj","_xhKTfxj","_BKTfxj","_yHjfxj","_MTTfxj","_xnTTfxj","_kTTfxj","_ExbTfxj","_rxbTfxj","_txbTfxj","_EKTfxj","_SKTfxj","_ytjfxj","_Kcjfxj","_Qcjfxj","_xaxkjfxj","_uHjfxj","_QHjfxj","_xepjfxj","_xbYjfxj","_gtjfxj","_xbcjfxj","_pcjfxj","_Sxkjfxj","_MHjfxj","_xmHjfxj","_npjfxj","_xotjfxj","_Gcjfxj","_ycjfxj","_Jxkjfxj","_xlHjfxj","_xgHjfxj","_xipjfxj","_qcjfxj","_ncjfxj","_Zxkjfxj","_vxkjfxj","_GHjfxj","_Rpjfxj","_epjfxj","_Zcjfxj","_Pcjfxj","_Kxkjfxj","_Nxkjfxj","_bHjfxj","_yHjfxj","_BKTfxj","_Wpjfxj","_xhcjfxj","_Bcjfxj","_uxkjfxj","_yxkjfxj","_iHjfxj","_xlpjfxj","_ypjfxj","_Mcjfxj","_mcjfxj","_bxkjfxj","_Qxkjfxj","_WHjfxj","_Gpjfxj","_zYjfxj","_xlcjfxj","_xecjfxj","_xjxkjfxj","_xcxkjfxj","_wHjfxj","_Ipjfxj","_Upjfxj","_dcjfxj","_Wcjfxj","_sxkjfxj","_xkxkjfxj","_FHjfxj","_apjfxj","_xdYjfxj","_bcjfxj","_lxkjfxj","_xmxkjfxj","_nHjfxj","_lpjfxj","_cpjfxj","_xfYjfxj","_Xcjfxj","_xdxkjfxj","_Uxkjfxj","_fHjfxj","_upjfxj","_Ypjfxj","_iYjfxj","_xfcjfxj","_Exkjfxj","_exkjfxj","_Qxkjfxj","_PHjfxj","_qpjfxj","_Dpjfxj","_bYjfxj","_fcjfxj","_Cxkjfxj","_Dxkjfxj","_XHjfxj","_Apjfxj","_xmpjfxj","_GYjfxj","_xjcjfxj","_xhxkjfxj","_mxkjfxj","_sHjfxj","_Epjfxj","_vpjfxj","_xjYjfxj","_rcjfxj","_Txkjfxj","_kxkjfxj","_xfHjfxj","_xhpjfxj","_kpjfxj","_nYjfxj","_acjfxj","_xbxkjfxj","_zHjfxj","_xaHjfxj","_xaHjfxj","_xbpjfxj","_AYjfxj","_rYjfxj","_Lcjfxj","_Pxkjfxj","_xdHjfxj","_HHjfxj","_Jpjfxj","_dYjfxj","_xmYjfxj","_Axkjfxj","_EYjfxj","_fxkjfxj","_WYjfxj","_Rxgjfxj","_EHjfxj","_nxgjfxj","_kHjfxj","_fpjfxj","_vxgjfxj","_cxkjfxj","_YYjfxj","_xnHjfxj","_sxgjfxj","_xdpjfxj","_Jxgjfxj","_hYjfxj","_txgjfxj","_PYjfxj","_dQjfxj","_Hxkjfxj","_gYjfxj","_SHjfxj","_jxgjfxj","_Bpjfxj","_rxgjfxj","_Lxgjfxj","_xopjfxj","_VQjfxj","_JYjfxj","_xgxkjfxj","_aHjfxj","_jpjfxj","_gpjfxj","_xaYjfxj","_Ixgjfxj","_Cxgjfxj","_zxgjfxj","_gxkjfxj","_NHjfxj","_bxgjfxj","_Xpjfxj","_Nxgjfxj","_Yxgjfxj","_IYjfxj","_TQjfxj","_aYjfxj","_xdxgjfxj","_AHjfxj","_pHjfxj","_xjxgjfxj","_xjpjfxj","_mxgjfxj","_mxgjfxj","_yxgjfxj","_qYjfxj","_sQjfxj","_FYjfxj","_UVTfxj","_METfxj","_GxdTfxj","_xgETfxj","_IMTfxj","_nlTfxj","_iMTfxj","_lVTfxj","_xixjTfxj","_yxjTfxj","_xbGTfxj","_LGTfxj","_VnTfxj","_xnnTfxj","_UnTfxj","_FxjTfxj","_FxjTfxj","_QxjTfxj","_bGTfxj","_HGTfxj","_CnTfxj","_NnTfxj","_gnTfxj","_gxjTfxj","_WxjTfxj","_sGTfxj","_gGTfxj","_xlnTfxj","_NxjTfxj","_xgnTfxj","_xbXTfxj","_qGTfxj","_xaGTfxj","_yGTfxj","_TnTfxj","_enTfxj","_ZXTfxj","_XXTfxj","_xexjTfxj","_anTfxj","_zXTfxj","_xoxjTfxj","_xexjTfxj","_anTfxj","_xjGTfxj","_bXTfxj","_bXTfxj","_xiXTfxj","_cGTfxj","_HXTfxj","_MnTfxj","_lETfxj","_xfxdTfxj","_xkETfxj","_lMTfxj","_xnlTfxj","_SMTfxj","_RVTfxj","_LMTfxj","_huTfxj","_NVTfxj","_dxdTfxj","_yxhTfxj","_JETfxj","_yxdTfxj","_xfMTfxj","_ElTfxj","_xmMTfxj","_UlTfxj","_BVTfxj","_AuTfxj","_RETfxj","_zPIfxj","_xeETfxj","_xbnIfxj","_MlTfxj","_clTfxj","_fVTfxj","_ZxdTfxj","_lsIfxj","_PETfxj","_xcETfxj","_yKIfxj","_EsIfxj","_XlTfxj","_xhVTfxj","_qsIfxj","_IsIfxj","_vVTfxj","_xhlTfxj","_CxdTfxj","_isIfxj","_xdMTfxj","_AsIfxj","_xaMTfxj","_zETfxj","_xaETfxj","_xoxdTfxj","_hVTfxj","_mVTfxj","_xnMTfxj","_uETfxj","_gETfxj","_JlTfxj","_YVTfxj","_xlVTfxj","_WxdTfxj","_EMTfxj","_JMTfxj","_jETfxj","_LETfxj","_KlTfxj","_AVTfxj","_aVTfxj","_MxdTfxj","_pxdTfxj","_XMTfxj","_EETfxj","_HETfxj","_GlTfxj","_EVTfxj","_cVTfxj","_xaxdTfxj","_KETfxj","_yETfxj","_xflTfxj","_uVTfxj","_xkVTfxj","_xnxdTfxj","_qMTfxj","_QxhTfxj","_xiETfxj","_ZlTfxj","_Msxgwxj","_DlTfxj","_xjPxgwxj","_XVTfxj","_hxdTfxj","_UxdTfxj","_VETfxj","_eETfxj","_ClTfxj","_xolTfxj","_xiVTfxj","_FxdTfxj","_gxhTfxj","_pETfxj","_blTfxj","_DETfxj","_zVTfxj","_xmVTfxj","_xdETfxj","_slTfxj","_IVTfxj","_xeVTfxj","_KxdTfxj","_YxdTfxj","_PMTfxj","_xoxhTfxj","_xmETfxj","_xllTfxj","_plTfxj","_SVTfxj","_lxdTfxj","_xkxdTfxj","_xjMTfxj","_eMTfxj","_VxdTfxj","_xfETfxj","_xgxdTfxj","_kETfxj","_nMTfxj","_TlTfxj","_NMTfxj","_QlTfxj","_yMTfxj","_JVTfxj","_kxcIfxj","_xiCTfxj","_xgdTfxj","_CxlTfxj","_gCTfxj","_xixlTfxj","_ujTfxj","_RCTfxj","_xajTfxj","_xkjTfxj","_CCTfxj","_JCTfxj","_gdTfxj","_jxlTfxj","_LCTfxj","_xdjTfxj","_FxlTfxj","_xnjTfxj","_hCTfxj","_uCTfxj","_HjTfxj","_NCTfxj","_ydTfxj","_QCTfxj","_sxlTfxj","_NxlTfxj","_jjTfxj","_JjTfxj","_ICTfxj","_KCTfxj","_cjTfxj","_RxlTfxj","_MxlTfxj","_rxlTfxj","_ACTfxj","_aCTfxj","_UCTfxj","_VjTfxj","_GYzfxj","_Pxgzfxj","_GQzfxj","_Kyzfxj","_Mgzfxj","_MxjNwxj","_xoxjNwxj","_aGNwxj","_xnnNwxj","_xhXNwxj","_LXNwxj","_wxfNwxj","_DbNwxj","_mxjNwxj","_xfGNwxj","_ZnNwxj","_xgnNwxj","_xeXNwxj","_bxfNwxj","_kYzfxj","_vxgzfxj","_WQzfxj","_xoyzfxj","_xagzfxj","_fxozfxj","_xlAIfxj","_xkxozfxj","_DAIfxj","_WYzfxj","_xmxgzfxj","_cQzfxj","_xeyzfxj","_Fgzfxj","_SPiwxj","_xewiwxj","_rfiwxj","_xaxniwxj","_nBiwxj","_wiiwxj","_CSiwxj","_JYzfxj","_axgzfxj","_HQzfxj","_Qyzfxj","_tgzfxj","_Dxozfxj","_xgAIfxj","_xcbNwxj","_kxjNwxj","_iGNwxj","_snNwxj","_hXNwxj","_xmXNwxj","_sxfNwxj","_nJNwxj","_TrNwxj","_xmaNwxj","_pxiNwxj","_xnFNwxj","_PmNwxj","_xfJNwxj","_ZrNwxj","_xcrNwxj","_xiaNwxj","_xnxiNwxj","_xlFNwxj","_hmNwxj","_bJNwxj","_RrNwxj","_krNwxj","_raNwxj","_fxiNwxj","_TFNwxj","_AmNwxj","_GJNwxj","_xbrNwxj","_ZaNwxj","_DaNwxj","_DxiNwxj","_WFNwxj","_jmNwxj","_XJNwxj","_PrNwxj","_AaNwxj","_eaNwxj","_vxiNwxj","_fFNwxj","_MmNwxj","_JJNwxj","_drNwxj","_YrNwxj","_YaNwxj","_LxiNwxj","_xiFNwxj","_GmNwxj","_uJNwxj","_xgJNwxj","_WrNwxj","_PaNwxj","_TxiNwxj","_IFNwxj","_kFNwxj","_vWiwxj","_xnxeiwxj","_xiNiwxj","_lviwxj","_Yviwxj","_xeeiwxj","_Xxmiwxj","_XWiwxj","_Gxeiwxj","_VNiwxj","_pNiwxj","_vviwxj","_feiwxj","_xlxmiwxj","_dYzfxj","_qxgzfxj","_xhyzfxj","_AQzfxj","_pyzfxj","_cgzfxj","_Qxozfxj","_xfYzfxj","_fxgzfxj","_xnQzfxj","_Pyzfxj","_Dgzfxj","_xnxozfxj","_CAIfxj","_xmWiwxj","_Leiwxj","_fxmiwxj","_Bxeiwxj","_TNiwxj","_yxmiwxj","_qLiwxj","_hviwxj","_xnLiwxj","_Hviwxj","_kxgzfxj","_aAIfxj","_Ayzfxj","_xjhIfxj","_kyzfxj","_yhIfxj","_egzfxj","_xfRIfxj","_LRIfxj","_ixozfxj","_uYzfxj","_Sxozfxj","_xlxgzfxj","_jAIfxj","_pQzfxj","_MhIfxj","_xiyzfxj","_mhIfxj","_igzfxj","_MRIfxj","_NYzfxj","_NYzfxj","_Kxozfxj","_Fxgzfxj","_xnAIfxj","_vQzfxj","_BhIfxj","_QhIfxj","_Jyzfxj","_nRIfxj","_Pgzfxj","_YWiwxj","_Heiwxj","_Pxmiwxj","_cxeiwxj","_SAIfxj","_gxmiwxj","_eNiwxj","_hLiwxj","_Pviwxj","_heiwxj","_PLiwxj","_xdxhcwxj","_Dxhcwxj","_SEcwxj","_Clcwxj","_Txhcwxj","_xhEcwxj","_xkEcwxj","_Blcwxj","_SWiwxj","_nxeiwxj","_uNiwxj","_xoNiwxj","_blcwxj","_Mxhcwxj","_hEcwxj","_qVcwxj","_UVcwxj","_DEcwxj","_mlcwxj","_nxhcwxj","_uVcwxj","_ZEcwxj","_QEcwxj","_xgVcwxj","_XYzfxj","_xdxgzfxj","_Sxgzfxj","_UQzfxj","_tyzfxj","_sMcwxj","_xlxhcwxj","_xoxhcwxj","_cEcwxj","_flcwxj","_BQiwxj","_zyiwxj","_xcyiwxj","_xigiwxj","_Mxoiwxj","_xkxoiwxj","_JASwxj","_xbhSwxj","_xiQiwxj","_xbyiwxj","_zgiwxj","_xkgiwxj","_xfxoiwxj","_MASwxj","_DASwxj","_nhSwxj","_vmxgwxj","_Sxexgwxj","_jNxgwxj","_dvxgwxj","_jexgwxj","_wxmxgwxj","_tDxgwxj","_xckxgwxj","_xeCIfxj","_Zxhcwxj","_xhjIfxj","_BjIfxj","_xcjIfxj","_BTIfxj","_xgTIfxj","_xgTIfxj","_xjQiwxj","_qyiwxj","_bQiwxj","_CASwxj","_Iyiwxj","_xeASwxj","_Dyiwxj","_xjhSwxj","_Lgiwxj","_lRSwxj","_Txoiwxj","_xaRSwxj","_Kxoiwxj","_PQiwxj","_zASwxj","_Kyiwxj","_LASwxj","_Agiwxj","_xnhSwxj","_kgiwxj","_xfQiwxj","_xixjIfxj","_Eyiwxj","_kxjIfxj","_kxjIfxj","_Wgiwxj","_TnIfxj","_rxoiwxj","_txjIfxj","_AASwxj","_AGIfxj","_BGIfxj","_WASwxj","_shSwxj","_exjIfxj","_xbnIfxj","_zPIfxj","_UxfIfxj","_xbXIfxj","_zxfIfxj","_yPIfxj","_bPIfxj","_iqSwxj","_xjZSwxj","_yqSwxj","_xjESwxj","_rqSwxj","_gqSwxj","_SZSwxj","_yZSwxj","_nxhSwxj","_YxhSwxj","_WESwxj","_xaDIfxj","_FkIfxj","_NUIfxj","_ixcIfxj","_rLIfxj","_BqSwxj","_xhZSwxj","_sESwxj","_xcxhSwxj","_wZSwxj","_FESwxj","_HZSwxj","_RlSwxj","_xllSwxj","_xjxhSwxj"]
    urls=[]
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }
    data={
        "url":f"https%3A%2F%2Fobam21.com",
        "mb_id": "part1020",
        "mb_password": "part1020"
    }
    yuanurl=f"https://pf.kakao.com/"
    namz=re.compile(r'<head>.*?<title>(?P<biaoti>.*?)</title>',re.S)
    f=open("haizai.csv",mode="w",encoding="utf-8")
    csvwriter=csv.writer(f)
#for i in range(100):
with ThreadPoolExecutor(2) as t:
    for yigeid in allid:
        xlj=yuanurl+yigeid
        t.submit(download_one_page,xlj,yigeid)



    # #print(dl.text)
        
    # resp=session.get(yurl, headers=headers)
    # resp.encoding='utf-8'#指定字符集
    # #print(resp.text)

    # for src in srcs:
    #     jshref=src.xpath('./center/a/@href')[0] #링크주소들
    #     mz=src.xpath('./div[4]/div[1]/a/text()')
    #     weizhi=src.xpath('./div[6]/div[1]/span[2]/text()')
    #     #cljs="".join(jshref).split("(",-1)[1]
    #     #cljs=cljs.split(")",-1)[0]
    #     if jshref !=[카카오톡채널 - 프로필이초기화되었습니다]:
    #         mz="".join(mz).replace("/","").replace("-","").strip()
    #         weizhi="".join(weizhi).replace("/","").replace("-","").strip()
    #         jshref="".join(jshref).replace("/","").replace("-","").strip()
    #         csvwriter.writerow([mz+" ",weizhi+" ",jshref])
    #     time.sleep(1)
    # print("all ok")

