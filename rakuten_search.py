import rakuten_search_lib as RSL

rsc = RSL.RakutenSearchCore()
rsc.Index()
#rsc.GoLoginPage()
rsc.Login()
rsc.Search()
rsc.Quit()

print("rakuten search end")
