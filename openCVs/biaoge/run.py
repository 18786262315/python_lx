import bg_sb,er_zhihua,pst
imge = R"C:\Users\Administrator\Desktop\b8c887b9828d46cfa9160edf02c0373c.jpg"
# urls = "http://192.168.0.145:9998/broke-manager-service/siteplan/updateSiteContent"
urls = "http://api.singmap.com/broke-manager-service/siteplan/updateSiteContent"
imge = er_zhihua.er_zhi(imge)
cont  = bg_sb.lk_mg(imge)
pst.pdt_wb(urls,cont)






