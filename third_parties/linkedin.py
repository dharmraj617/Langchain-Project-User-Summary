import os
import requests


def scrape_info_from_linkdin(linkedin_profile_url: str):
    """
    scrape information from LinkedIn profiles,
    Manually scrape information from LinkedIn profiles.
    """
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + os.environ.get("PROXYCURL_API_KEY")}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data