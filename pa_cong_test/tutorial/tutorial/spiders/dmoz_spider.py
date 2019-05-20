import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["testccweb.com"]
    start_urls = [
        "http://www.testccweb.com/",
        "http://api.testccweb.com"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'w') as f:
            f.write(response.body)








<p>&nbsp;</p>
<table border="0" width="100%" cellspacing="0" cellpadding="20">
<tbody>
<tr>
<td style="text-align: center; font-size: 10px; font-family: Arial;">&nbsp;</td>
</tr>
</tbody>
</table>
<table style="background-color: #545454;" border="0" width="100%" cellspacing="0" cellpadding="20">
<tbody>
<tr>
<td align="center" valign="top">
<table style="text-align: left;" border="0" width="670" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="font-size: 0pt; line-height: 0pt; width: 10px;">&nbsp;</td>
<td style="font-size: 0pt; line-height: 0pt;"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/top.jpg" alt="" width="650" height="7" /></td>
<td style="font-size: 0pt; line-height: 0pt; width: 10px;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td style="font-family: Arial, sans-serif; font-size: 11px; text-align: left; white-space: nowrap; padding: 5px 0px 10px 20px; background-color: #000000;"><a style="color: #de1a32; text-decoration: none;" href="${CompanyWebsiteUrl}">${CompanyWebsiteUrl}</a></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>
<div style="font-size: 0pt; line-height: 1pt; min-height: 1px; margin: 0px; background-color: #ffffff;">&nbsp;</div>
<div style="font-size: 0pt; line-height: 1pt; min-height: 1px; margin: 0px; background-color: #8c8c8c;">&nbsp;</div>
</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 10px;">&nbsp;</td>
<td style="color: #de1a32; font-weight: bold; font-style: normal; font-variant: normal; font-size: 30px; line-height: normal; font-family: Arial, sans-serif; padding-left: 20px; background-color: #ffffff;">${PropertyName}</td>
<td style="padding: 0px 10px; text-align: right; vertical-align: middle; width: 150px; background-color: #ffffff;">
<img alt="" width="150" src="${CompanyLogoUrl}" style="max-width: 150px;" /> 
</td>
<td style="width: 10px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="font-size: 0pt; line-height: 0pt; text-align: left; padding: 0px 10px;"><img src="http://img.singmap.com/upload/broke/otherimg/shadow_header.jpg" alt="" /></td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="font-size: 0pt; width: 10px; line-height: 0pt; text-align: left;">&nbsp;</td>
<td style="width: 650px; background-color: #ffffff;">
<table style="width: 100%;">
<tbody>
<tr>
<td style="width: 20px;">&nbsp;</td>
<td style="padding-top: 10px; font-size: 12px; font-family: Arial, sans-serif;">${ToName},<br />${WelcomeMsg}</td>
<td style="width: 20px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
<td style="font-size: 0pt; width: 10px; line-height: 0pt; text-align: left;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="line-height: 0pt; width: 10px;" valign="bottom"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/ldot2.jpg" alt="" width="10" height="6" /></td>
<td style="background-color: #ffffff;">&nbsp;</td>
<td style="line-height: 0pt; width: 10px;" valign="bottom"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/rdot2.jpg" alt="" width="10" height="6" /></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="background-color: #de1a32;">
<table style="background-color: #de1a32;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 30px;">&nbsp;</td>
<td style="font-weight: bold; font-size: 20px; color: #ffffff; line-height: 24px; font-family: Arial; text-align: left; background-color: #de1a32;">Unit ${UnitName}</td>
<td style="width: 30px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="font-size: 0pt; line-height: 0pt; text-align: left; padding: 0px 10px;"><img src="http://img.singmap.com/upload/broke/otherimg/shadow_title.jpg" alt="" /></td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 10px;">&nbsp;</td>
<td style="width: 650px; background-color: #ffffff;">
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 20px;">&nbsp;</td>
<td style="vertical-align: top; width: 305px; padding-top: 10px;">
<table style="font-family: Arial, sans-serif;" border="0" width="100%" cellspacing="0" cellpadding="5">
<tbody>
<tr>
<td style="width: 100px;">Area</td>
<td style="font-weight: bold;">${UnitArea}</td>
</tr>
<tr>
<td>Type</td>
<td style="font-weight: bold;">${UnitType}</td>
</tr>
<tr>
<td>Floor</td>
<td style="font-weight: bold;">${UnitFloor}</td>
</tr>
<tr>
<td>Plan</td>
<td style="font-weight: bold;">${UnitFloorPlan}</td>
</tr>
</tbody>
</table>
</td>
<td style="width: 305px; padding-top: 10px; text-align: center; font-family: Arial, sans-serif; font-size: 8pt;"><a href="${UnitFloorPlanUrl}" target="_blank" rel="noopener"> <img style="max-width: 280px; border-style: none;" src="${UnitFloorPlanUrl}" alt="Floor Plan Image" width="280" /></a> <!-- <br/> 户型图参数获取错误。 --> Click image to enlarge</td>
<td style="width: 20px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
<td style="width: 10px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="line-height: 0pt; width: 10px;" valign="bottom"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/ldot2.jpg" alt="" width="10" height="6" /></td>
<td style="background-color: #ffffff;">&nbsp;</td>
<td style="line-height: 0pt; width: 10px;" valign="bottom"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/rdot2.jpg" alt="" width="10" height="6" /></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="background-color: #de1a32;">
<table style="background-color: #de1a32;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 30px;">&nbsp;</td>
<td style="font-weight: bold; font-size: 20px; color: #ffffff; line-height: 24px; font-family: Arial; text-align: left; background-color: #de1a32;">Images</td>
<td style="width: 30px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="font-size: 0pt; line-height: 0pt; text-align: left; padding: 0px 10px;"><img src="http://img.singmap.com/upload/broke/otherimg/shadow_title.jpg" alt="" /></td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="font-size: 0pt; width: 10px; line-height: 0pt; text-align: left;">&nbsp;</td>
<td style="width: 650px; padding-top: 10px; background-color: #ffffff;">
<table style="font-family: Arial, sans-serif;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 20px;">&nbsp;</td>
<td style="width: 20px;"><a href="#"> <img src="http://img.singmap.com/upload/broke/otherimg/button_left.gif" alt="" width="20px" height="87px" /> </a></td>
<td>${PropertyImage}</td>
<td style="width: 20px;"><a href="#"> <img src="http://img.singmap.com/upload/broke/otherimg/button_right.gif" alt="" width="20px" height="87px" /> </a></td>
<td style="width: 20px;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td style="font-size: 9pt;">&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
</td>
<td style="font-size: 0pt; width: 10px; line-height: 0pt; text-align: left;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="line-height: 0pt; width: 10px;" valign="bottom"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/ldot2.jpg" alt="" width="10" height="6" /></td>
<td style="background-color: #ffffff;">&nbsp;</td>
<td style="line-height: 0pt; width: 10px;" valign="bottom"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/rdot2.jpg" alt="" width="10" height="6" /></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="background-color: #de1a32;">
<table style="background-color: #de1a32;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 30px;">&nbsp;</td>
<td style="font-weight: bold; font-size: 20px; color: #ffffff; line-height: 24px; font-family: Arial; text-align: left; background-color: #de1a32;">Project Information</td>
<td style="width: 30px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="font-size: 0pt; line-height: 0pt; text-align: left; padding: 0px 10px;"><img src="http://img.singmap.com/upload/broke/otherimg/shadow_title.jpg" alt="" /></td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="font-size: 0pt; width: 10px; line-height: 0pt; text-align: left;">&nbsp;</td>
<td style="padding-top: 10px; background-color: #ffffff;">
<table style="font-family: Arial, sans-serif;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 20px;">&nbsp;</td>
<td style="width: 150px; padding: 5px 0px;">Name</td>
<td style="font-weight: bold; padding: 5px 0px;">${PropertyName}</td>
<td style="width: 20px;">&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td style="padding: 5px 0px;">Developer</td>
<td style="font-weight: bold; padding: 5px 0px;">${PropertyDeveloper}</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td style="padding: 5px 0px;">Type</td>
<td style="font-weight: bold; padding: 5px 0px;">${PropertyType}</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td style="padding: 5px 0px;">Tenure</td>
<td style="font-weight: bold; padding: 5px 0px;">${PropertyTenure}</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td style="padding: 5px 0px;">Location</td>
<td style="font-weight: bold; padding: 5px 0px;">${PropertyLocation}</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td style="padding: 5px 0px;">Number of Units</td>
<td style="font-weight: bold; padding: 5px 0px;">${PropertyNumberOfUnits}</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<br />
<table style="font-family: Arial, sans-serif;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 20px;">&nbsp;</td>
<td style="width: 294px; vertical-align: top;"><span style="font-size: 20px; font-weight: bold; padding-right: 10px; color: #de1a32;">Amenities</span><br /><br />${PropertyNearbyAmenities}</td>
<!-- <td style="font-size: 0pt; line-height: 0pt; text-align: left; width: 1px; background-color: #dfdfdf;">
                                                                </td> -->
<td style="width: 295px; vertical-align: top; padding-left: 10px;"><span style="font-size: 20px; font-weight: bold; color: #de1a32;">Facilities</span> <br /><br />${PropertyFacilities}</td>
<td style="width: 20px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
<td style="width: 10px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 10px;">&nbsp;</td>
<td style="background-color: #ffffff;">&nbsp;</td>
<td style="width: 10px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 10px;">&nbsp;</td>
<td style="padding: 10px; background-color: #ffffff;"><em>Information herein is based on third party sources we believe reliable and we do not assure its accuracy or completeness. </em></td>
<td style="width: 10px;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table style="font-family: Arial, sans-serif;" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 10px;">&nbsp;</td>
<td style="padding: 20px; color: #ffffff; background-color: #000000;">
<table>
<tbody>
<tr>
<td><img src="${photo}" alt="photo" width="90" height="120" /></td>
<td style="padding: 15px; color: #ffffff;">${signature}</td>
</tr>
</tbody>
</table>
</td>
<td style="width: 10px;">&nbsp;</td>
</tr>
<tr>
<td style="font-size: 0pt; line-height: 0pt;">&nbsp;</td>
<td style="font-size: 0pt; line-height: 0pt;"><img style="border-width: 0px; border-style: solid;" src="http://img.singmap.com/upload/broke/otherimg/bottom.jpg" alt="" width="650" height="5" /></td>
<td style="font-size: 0pt; line-height: 0pt;">&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>