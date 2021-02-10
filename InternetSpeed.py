from speedtest import Speedtest
st = Speedtest()

print("Your download speed is ", st.download())
print("Your upload speed is", st.upload())