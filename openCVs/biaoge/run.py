import bg_sb,er_zhihua,pst
imge = R'C:\Users\Administrator\Desktop\siteplan2.jpg'
urls = "http://192.168.0.145:9998/broke-manager-service/siteplan/updateSiteContent"
imge = er_zhihua.er_zhi(imge)
cont  = bg_sb.lk_mg(imge)
pst.pdt_wb(urls,cont)






