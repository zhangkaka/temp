#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import json

def getList():
    data = '''
{"snatchNode_new": {"hosts": [], "children": ["dg-snatchNode_new"]}, "hk-user-system-service": ["hk-7", "hk-5"], "sg-ybf-nginx": ["sg-1"], "water-webServer": {"hosts": [], "children": ["hk-water-webServer"]}, "basket-score": {"hosts": [], "children": ["dg-basket-score", "hk-basket-score"]}, "hk-rbData-webServer": ["hk-7"], "hk-snookerDataProvider": ["hk-14", "hk-15"], "hk-app_html": ["hk-1"], "toutiao-news": {"hosts": [], "children": ["hk-toutiao-news"]}, "ybf-data-lineup": {"hosts": [], "children": ["hk-ybf-data-lineup"]}, "bonusServer": {"hosts": [], "children": ["hk-bonusServer"]}, "hk-odds-appServer": ["hk-7"], "hk-app-fileserver": ["hk-14"], "data-webServer": {"hosts": [], "children": ["dg-data-webServer", "vn-data-webServer", "hk-data-webServer"]}, "dg-basket-score": ["dg-5", "dg-4"], "football-heart-water": {"hosts": [], "children": ["hk-football-heart-water"]}, "ybf-server": {"hosts": [], "children": ["hk-ybf-server"]}, "ybf-oss": {"hosts": [], "children": ["hk-ybf-oss"]}, "hk-basket": ["hk-6", "hk-1"], "chatServer-CMS-singapore": {"hosts": [], "children": ["hk-chatServer-CMS-singapore"]}, "th-tj": ["th-1", "th-2"], "dg-tp": ["dg-2"], "news-web": {"hosts": [], "children": ["dg-news-web", "vn-news-web", "hk-news-web", "th-news-web", "sg-news-web"]}, "dg-user-web": ["dg-4"], "sg-img-server": ["sg-2"], "redisCleaner": {"hosts": [], "children": ["dg-redisCleaner", "vn-redisCleaner", "th-redisCleaner"]}, "information-server": {"hosts": [], "children": ["hk-information-server"]}, "hk-football": ["hk-6", "hk-1"], "vn-omsiceserver": ["vn-6", "vn-11"], "dg-snk": ["dg-4", "dg-5", "dg-6", "dg-1", "dg-2", "dg-3"], "tp": {"hosts": [], "children": ["dg-tp"]}, "snk": {"hosts": [], "children": ["dg-snk", "hk-snk"]}, "vn-data-webServer": ["vn-1"], "basketball-app": {"hosts": [], "children": ["hk-basketball-app"]}, "hk-tj": ["hk-6", "hk-1"], "vn-resources": ["vn-1", "vn-2"], "data-balls-server": {"hosts": [], "children": ["hk-data-balls-server"]}, "timelyScore-webServerjj": {"hosts": [], "children": ["dg-timelyScore-webServerjj"]}, "betgo-bms": {"hosts": [], "children": ["hk-betgo-bms"]}, "sg-appvn-north_html": ["sg-10", "sg-11"], "user-web": {"hosts": [], "children": ["dg-user-web", "hk-user-web"]}, "th-img-server": ["th-4"], "unifiedAgent-server": {"hosts": [], "children": ["dg-unifiedAgent-server", "vn-unifiedAgent-server", "th-unifiedAgent-server", "sg-unifiedAgent-server"]}, "hk-static": ["hk-1", "hk-6"], "hk-ybf-data-lineup": ["hk-6"], "mobile-user-web-app": {"hosts": [], "children": ["dg-mobile-user-web-app"]}, "sg-basket": ["sg-1"], "vn-football": ["vn-1", "vn-2"], "recommends": {"hosts": [], "children": ["dg-recommends", "vn-recommends", "hk-recommends", "th-recommends", "sg-recommends"]}, "data-balls-analysis": {"hosts": [], "children": ["hk-data-balls-analysis"]}, "snookerDataProvider": {"hosts": [], "children": ["hk-snookerDataProvider"]}, "hk-ybf_sprots_recommend": ["hk-9", "hk-10"], "mobile-promotion-web-app": {"hosts": [], "children": ["dg-mobile-promotion-web-app"]}, "sg-timelyScore-webServer": ["sg-2", "sg-1"], "chatServer1": {"hosts": [], "children": ["dg-chatServer1"]}, "basketballManage": {"hosts": [], "children": ["hk-basketballManage"]}, "_meta": {"hostvars": {"hk-8": {"hostname": "hk-8"}, "hk-9": {"hostname": "hk-9"}, "vn-4": {"hostname": "vn-4"}, "hk-1": {"hostname": "hk-1"}, "hk-2": {"hostname": "hk-2"}, "hk-3": {"hostname": "hk-3"}, "hk-4": {"hostname": "hk-4"}, "hk-5": {"hostname": "hk-5"}, "hk-6": {"hostname": "hk-6"}, "hk-7": {"hostname": "hk-7"}, "dg-1": {"hostname": "dg-1"}, "dg-2": {"hostname": "dg-2"}, "dg-3": {"hostname": "dg-3"}, "dg-4": {"hostname": "dg-4"}, "dg-5": {"hostname": "dg-5"}, "dg-6": {"hostname": "dg-6"}, "dg-7": {"hostname": "dg-7"}, "dg-8": {"hostname": "dg-8"}, "dg-9": {"hostname": "dg-9"}, "hk-22": {"hostname": "hk-22"}, "hk-21": {"hostname": "hk-21"}, "hk-20": {"hostname": "hk-20"}, "vn-9": {"hostname": "vn-9"}, "vn-10": {"hostname": "vn-10"}, "th-10": {"hostname": "th-10"}, "vn-6": {"hostname": "vn-6"}, "vn-12": {"hostname": "vn-12"}, "vn-11": {"hostname": "vn-11"}, "sg-4": {"hostname": "sg-4"}, "dg-19": {"hostname": "dg-19"}, "sg-7": {"hostname": "sg-7"}, "dg-12": {"hostname": "dg-12"}, "dg-13": {"hostname": "dg-13"}, "dg-10": {"hostname": "dg-10"}, "dg-11": {"hostname": "dg-11"}, "dg-16": {"hostname": "dg-16"}, "dg-14": {"hostname": "dg-14"}, "dg-15": {"hostname": "dg-15"}, "hk-12": {"hostname": "hk-12"}, "hk-13": {"hostname": "hk-13"}, "hk-10": {"hostname": "hk-10"}, "hk-11": {"hostname": "hk-11"}, "hk-16": {"hostname": "hk-16"}, "hk-17": {"hostname": "hk-17"}, "hk-14": {"hostname": "hk-14"}, "hk-15": {"hostname": "hk-15"}, "vn-1": {"hostname": "vn-1"}, "hk-18": {"hostname": "hk-18"}, "hk-19": {"hostname": "hk-19"}, "sg-6": {"hostname": "sg-6"}, "th-7": {"hostname": "th-7"}, "th-6": {"hostname": "th-6"}, "th-5": {"hostname": "th-5"}, "th-4": {"hostname": "th-4"}, "th-3": {"hostname": "th-3"}, "th-2": {"hostname": "th-2"}, "th-1": {"hostname": "th-1"}, "vn-8": {"hostname": "vn-8"}, "sg-11": {"hostname": "sg-11"}, "sg-10": {"hostname": "sg-10"}, "vn-5": {"hostname": "vn-5"}, "sg-12": {"hostname": "sg-12"}, "vn-3": {"hostname": "vn-3"}, "vn-2": {"hostname": "vn-2"}, "th-9": {"hostname": "th-9"}, "th-8": {"hostname": "th-8"}, "sg-1": {"hostname": "sg-1"}, "vn-7": {"hostname": "vn-7"}, "sg-3": {"hostname": "sg-3"}, "sg-2": {"hostname": "sg-2"}, "sg-5": {"hostname": "sg-5"}, "dg-22": {"hostname": "dg-22"}, "dg-21": {"hostname": "dg-21"}, "dg-20": {"hostname": "dg-20"}, "sg-9": {"hostname": "sg-9"}, "sg-8": {"hostname": "sg-8"}}}, "th-recommends": ["th-1", "th-2"], "hk-chatServer-CMS": ["hk-14"], "hk-omsiceserver": ["hk-14", "hk-15"], "sg-recommends": ["sg-1"], "nodeManage": {"hosts": [], "children": ["hk-nodeManage"]}, "dg-ybf_sprots_recommend": ["dg-1", "dg-2"], "ybf-oss-spc(\u6682\u505c)": {"hosts": [], "children": ["hk-ybf-oss-spc(\u6682\u505c)"]}, "th-basket": ["th-1", "th-2"], "oms": {"hosts": [], "children": ["hk-oms"]}, "hk-oms": ["hk-14"], "hk-basketballManage": ["hk-11"], "basket": {"hosts": [], "children": ["dg-basket", "vn-basket", "hk-basket", "th-basket", "sg-basket"]}, "th-unifiedAgent-server": ["th-7", "th-8"], "sg-static": ["sg-1"], "sports_activemq": {"hosts": [], "children": ["hk-sports_activemq"]}, "sg-football": ["sg-1"], "static": {"hosts": [], "children": ["dg-static", "vn-static", "hk-static", "th-static", "sg-static"]}, "th-app_activemq": ["th-6"], "dg-basketball-webServer-task": ["dg-5"], "sg-resources": ["sg-1"], "tj": {"hosts": [], "children": ["dg-tj", "vn-tj", "hk-tj", "th-tj", "sg-tj"]}, "hk-eventCenter": ["hk-11"], "hk-storageManage": ["hk-11"], "th-chatServer": ["th-7"], "dg-football": ["dg-1", "dg-2", "dg-3", "dg-4", "dg-5", "dg-6"], "sg-userres": ["sg-1"], "hk-data-balls-server": ["hk-8"], "dg-ybf-tj-web": ["dg-1", "dg-2"], "water-server": {"hosts": [], "children": ["hk-water-server"]}, "dg-static": ["dg-4", "dg-5", "dg-2", "dg-3", "dg-6", "dg-1"], "hk-matchPushServer": ["hk-14"], "hk-match_sp_data_web": ["hk-10"], "dubbo-admin": {"hosts": [], "children": ["hk-dubbo-admin"]}, "th-resources": ["th-1", "th-2"], "basket_server": {"hosts": [], "children": ["dg-basket_server"]}, "hk-information-provider1": ["hk-14"], "hk-data-server": ["hk-6", "hk-8"], "ybf-data-zqjc": {"hosts": [], "children": ["hk-ybf-data-zqjc"]}, "vn-recommends": ["vn-1", "vn-2"], "dg-tj": ["dg-1", "dg-2", "dg-3", "dg-4", "dg-5", "dg-6"], "sg-appDataPushServer": ["sg-9"], "hk-bonusServer": ["hk-14"], "vn-img-server": ["vn-4"], "vn-appvn-north_html": ["vn-1", "vn-2"], "hk-oss_bet_game": ["hk-9"], "betgo": {"hosts": [], "children": ["dg-betgo"]}, "dg-resources": ["dg-21", "dg-22", "dg-20", "dg-19"], "hk-ybf-oss": ["hk-7"], "vn-app_activemq": ["vn-6", "vn-11"], "vn-appDataPushServer": ["vn-6", "vn-11"], "dg-grabData-basketball": ["dg-4"], "hk-img-server": ["hk-7"], "sg-appvn-south_html": ["sg-10", "sg-11"], "hk-sports_activemq": ["hk-6", "hk-7"], "hk-news-web": ["hk-5", "hk-6"], "vn-userres": ["vn-1", "vn-2"], "dg-betgo": ["dg-7", "dg-8"], "hk-bet_game_web": ["hk-9"], "hk-water-webServer": ["hk-2"], "rbData-webServer": {"hosts": [], "children": ["hk-rbData-webServer"]}, "hk-snatchNode": ["hk-11"], "th-timelyScore-webServer": ["th-4", "th-5"], "hk-tennis": ["hk-6", "hk-1"], "dg-snatchNode_new": ["dg-6"], "ybf-tj-data": {"hosts": [], "children": ["hk-ybf-tj-data"]}, "dg-basket-data-server": ["dg-5"], "hk-data-balls-analysis": ["hk-5"], "snatchNode": {"hosts": [], "children": ["dg-snatchNode", "hk-snatchNode"]}, "dg-redisCleaner": ["dg-10"], "th-appDataPushServer": ["th-6"], "hk-ybf-data-zqjc": ["hk-7"], "hk-rbReceive": ["hk-11"], "hk-toutiao-news": ["hk-7"], "dg-basket-data": ["dg-5", "dg-4"], "bet_game_server": {"hosts": [], "children": ["hk-bet_game_server"]}, "th-redisCleaner": ["th-6"], "dg-tennis": ["dg-22", "dg-21"], "dg-betgo1": ["dg-7", "dg-8"], "user-behavior-server": {"hosts": [], "children": ["hk-user-behavior-server"]}, "sg-chatServer": ["sg-4", "sg-6", "sg-8"], "hk-ybf_file_server": ["hk-5"], "ybf-data-snk": {"hosts": [], "children": ["hk-ybf-data-snk"]}, "basketball-bmc": {"hosts": [], "children": ["hk-basketball-bmc"]}, "app_html": {"hosts": [], "children": ["dg-app_html", "hk-app_html"]}, "hk-user-web": ["hk-7"], "football": {"hosts": [], "children": ["dg-football", "vn-football", "hk-football", "th-football", "sg-football"]}, "hk-ybf-tj-service": ["hk-9", "hk-10"], "active": {"hosts": [], "children": ["dg-active"]}, "information-provider": {"hosts": [], "children": ["hk-information-provider"]}, "appDataPushServer": {"hosts": [], "children": ["dg-appDataPushServer", "vn-appDataPushServer", "th-appDataPushServer", "sg-appDataPushServer"]}, "tennisDataProvider": {"hosts": [], "children": ["hk-tennisDataProvider"]}, "hk-bet_game_server": ["hk-10"], "appvn-south_html": {"hosts": [], "children": ["vn-appvn-south_html", "sg-appvn-south_html"]}, "hk-basket-score": ["hk-20"], "eventCenter": {"hosts": [], "children": ["hk-eventCenter"]}, "vn-timelyScore-webServer": ["vn-5", "vn-4"], "hk-information-provider": ["hk-15", "hk-14"], "information-provider1": {"hosts": [], "children": ["hk-information-provider1"]}, "vn-unifiedAgent-server": ["vn-11", "vn-7", "vn-9", "vn-10"], "dg-userres": ["dg-1", "dg-2", "dg-3", "dg-4", "dg-5", "dg-6"], "basketball-webServer-task": {"hosts": [], "children": ["dg-basketball-webServer-task"]}, "betgo1": {"hosts": [], "children": ["dg-betgo1"]}, "tennis": {"hosts": [], "children": ["dg-tennis", "hk-tennis"]}, "unifiedAgent-server1": {"hosts": [], "children": ["dg-unifiedAgent-server1", "vn-unifiedAgent-server1", "th-unifiedAgent-server1", "sg-unifiedAgent-server1"]}, "matchPushServer": {"hosts": [], "children": ["hk-matchPushServer"]}, "hk-ybf-tj-manageService": ["hk-7"], "hk-resources": ["hk-6", "hk-1"], "hk-timelyScore-webServer": ["hk-5", "hk-6"], "img-server": {"hosts": [], "children": ["dg-img-server", "vn-img-server", "hk-img-server", "th-img-server", "sg-img-server"]}, "bt_receive": {"hosts": [], "children": ["hk-bt_receive"]}, "th-userres": ["th-1", "th-2"], "dg-app_html": ["dg-1", "dg-6", "dg-16"], "vn-basket": ["vn-1", "vn-2"], "appvn-north_html": {"hosts": [], "children": ["vn-appvn-north_html", "sg-appvn-north_html"]}, "hk-football-heart-water": ["hk-7"], "sg-tj": ["sg-1"], "vn-appvn-south_html": ["vn-1", "vn-2"], "dg-timelyScore-webServerjj": ["dg-1"], "dg-news-web": ["dg-1", "dg-6", "dg-4", "dg-5", "dg-8", "dg-9", "dg-2", "dg-3", "dg-10"], "hk-sportSnatch_activemq": ["hk-11"], "hk-ybf-server": ["hk-6", "hk-8"], "hk-information-server": ["hk-14"], "sg-appth_html": ["sg-10", "sg-11", "sg-1"], "userres": {"hosts": [], "children": ["dg-userres", "vn-userres", "hk-userres", "th-userres", "sg-userres"]}, "data-balls-webServer": {"hosts": [], "children": ["dg-data-balls-webServer"]}, "dg-timelyScore-webServer": ["dg-1", "dg-2", "dg-6", "dg-3", "dg-8", "dg-9", "dg-10", "dg-4", "dg-5"], "dg-img-server": ["dg-6"], "data-server": {"hosts": [], "children": ["hk-data-server"]}, "vn-news-web": ["vn-4", "vn-5"], "dg-basket_server": ["dg-5"], "hk-bt_receive": ["hk-11"], "match_sp_data_web": {"hosts": [], "children": ["hk-match_sp_data_web"]}, "rbData-receive": {"hosts": [], "children": ["hk-rbData-receive"]}, "vn-redisCleaner": ["vn-6", "vn-11"], "dg-unifiedAgent-server": ["dg-7", "dg-9", "dg-8"], "dg-chatServer": ["dg-7", "dg-8"], "vn-chatServer": ["vn-7", "vn-9", "vn-11", "vn-10"], "sg-news-web": ["sg-2"], "sportSnatch_activemq": {"hosts": [], "children": ["hk-sportSnatch_activemq"]}, "hk-data-webServer": ["hk-6", "hk-8"], "hk-rbData-receive": ["hk-21", "hk-5"], "hk-basketball-bmc": ["hk-20"], "dg-appDataPushServer": ["dg-10"], "hk-ybf-oss-spc(\u6682\u505c)": ["hk-7"], "hk-userres": ["hk-6", "hk-1"], "hk-water-server": ["hk-2"], "hk-betgo-bms": ["hk-14"], "app-fileserver": {"hosts": [], "children": ["hk-app-fileserver"]}, "hk-dubbo-admin": ["hk-9"], "resources": {"hosts": [], "children": ["dg-resources", "vn-resources", "hk-resources", "th-resources", "sg-resources"]}, "hk-basketball-app": ["hk-20"], "dg-mobile-user-web-app": ["dg-7"], "hk-recommends": ["hk-6", "hk-1"], "dg-mobile-promotion-web-app": ["dg-7"], "basket-data": {"hosts": [], "children": ["dg-basket-data"]}, "snookerDataConvert": {"hosts": [], "children": ["hk-snookerDataConvert"]}, "ybf-server2": {"hosts": [], "children": ["hk-ybf-server2"]}, "hk-chatServer-CMS-singapore": ["hk-14"], "grabData-basketball": {"hosts": [], "children": ["dg-grabData-basketball"]}, "sg-unifiedAgent-server1": ["sg-4", "sg-8", "sg-6"], "dg-data-webServer": ["dg-1", "dg-2"], "dg-unifiedAgent-server1": ["dg-7", "dg-8", "dg-9"], "rbReceive": {"hosts": [], "children": ["hk-rbReceive"]}, "ybf_file_server": {"hosts": [], "children": ["hk-ybf_file_server"]}, "hk-ybf-server2": ["hk-6", "hk-8"], "basket-data-server": {"hosts": [], "children": ["dg-basket-data-server"]}, "analysis": {"hosts": [], "children": ["hk-analysis"]}, "vn-unifiedAgent-server1": ["vn-11", "vn-7", "vn-9", "vn-10"], "hk-snookerDataConvert": ["hk-14", "hk-15"], "bet_game_web": {"hosts": [], "children": ["hk-bet_game_web"]}, "hk-ybf-tj-data": ["hk-7"], "dg-recommends": ["dg-20", "dg-19"], "vn-tj": ["vn-1", "vn-2"], "ybf-tj-web": {"hosts": [], "children": ["dg-ybf-tj-web"]}, "th-static": ["th-1", "th-2"], "hk-tennisDataProvider": ["hk-14", "hk-15"], "sg-unifiedAgent-server": ["sg-4", "sg-6", "sg-8"], "dg-ybf-nginx": ["dg-1", "dg-2", "dg-3", "dg-4", "dg-5", "dg-6"], "ybf_sprots_recommend": {"hosts": [], "children": ["dg-ybf_sprots_recommend", "hk-ybf_sprots_recommend"]}, "dg-basket": ["dg-1", "dg-2", "dg-3", "dg-4", "dg-5", "dg-6"], "timelyScore-webServer": {"hosts": [], "children": ["dg-timelyScore-webServer", "vn-timelyScore-webServer", "hk-timelyScore-webServer", "th-timelyScore-webServer", "sg-timelyScore-webServer"]}, "hk-tennisDataConvert": ["hk-14"], "user-system-service": {"hosts": [], "children": ["hk-user-system-service"]}, "hk-user-behavior-server": ["hk-7"], "dg-active": ["dg-19", "dg-16"], "ybf-data-all": {"hosts": [], "children": ["hk-ybf-data-all"]}, "hk-analysis": ["hk-5"], "hk-ybf-data-all": ["hk-7"], "th-news-web": ["th-4", "th-5", "th-10"], "omsiceserver": {"hosts": [], "children": ["vn-omsiceserver", "hk-omsiceserver"]}, "th-appth_html": ["th-2", "th-1"], "appth_html": {"hosts": [], "children": ["th-appth_html", "sg-appth_html"]}, "dg-snatchNode": ["dg-6"], "basket-score-server": {"hosts": [], "children": ["dg-basket-score-server"]}, "dg-app_activemq": ["dg-10"], "chatServer-CMS": {"hosts": [], "children": ["hk-chatServer-CMS"]}, "ybf-tj-manageService": {"hosts": [], "children": ["hk-ybf-tj-manageService"]}, "storageManage": {"hosts": [], "children": ["hk-storageManage"]}, "dg-basket-score-server": ["dg-5"], "hk-ybf-data-snk": ["hk-7"], "chatServer": {"hosts": [], "children": ["dg-chatServer", "vn-chatServer", "th-chatServer", "sg-chatServer"]}, "vn-static": ["vn-1", "vn-2"], "hk-snk": ["hk-6", "hk-1"], "hk-omsdata": ["hk-14"], "odds-appServer": {"hosts": [], "children": ["hk-odds-appServer"]}, "ybf-tj-service": {"hosts": [], "children": ["hk-ybf-tj-service"]}, "omsdata": {"hosts": [], "children": ["hk-omsdata"]}, "th-unifiedAgent-server1": ["th-7", "th-8"], "tennisDataConvert": {"hosts": [], "children": ["hk-tennisDataConvert"]}, "th-football": ["th-1", "th-2"], "oss_bet_game": {"hosts": [], "children": ["hk-oss_bet_game"]}, "hk-nodeManage": ["hk-11"], "app_activemq": {"hosts": [], "children": ["dg-app_activemq", "vn-app_activemq", "th-app_activemq"]}, "dg-chatServer1": ["dg-7", "dg-8"], "ybf-nginx": {"hosts": [], "children": ["dg-ybf-nginx", "sg-ybf-nginx"]}, "dg-data-balls-webServer": ["dg-4", "dg-5"]}
'''
    print data

def getVars(host):
    data = {"_meta":{"hostvars" : {"dg-1":{"asdf":1234},"dg-2":{"asdf":5678},}}}
    print data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list',action='store_true',dest='list',help='get all hosts')
    parser.add_argument('--host',action='store',dest='host',help='get all hosts')
    args = parser.parse_args()

    if args.list:
        getList()

    if args.host:
        getVars(args.host)
