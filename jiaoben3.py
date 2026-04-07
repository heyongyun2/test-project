import requests
class heyongtao:
    def tests(self):
        urls="https://httpbin.org/post"
        jsons={
            "username":"testuser",
            "password":"123456"

            }
        res=requests.post(url=urls,json=jsons)
        print("状态码:",res.status_code)
        print("响应:",res.json())
if __name__=="__main__":
    test=heyongtao()
    test.tests()
    
    
