import speedtest

# change the number of threads for multi threaded test
threads = None

st = speedtest.Speedtest()
st.get_best_server()
download_speed = st.download(threads=threads)
upload_speed = st.upload(threads=threads)
st.results.share()

results_dict = st.results.dict()
print(results_dict['ping'])

