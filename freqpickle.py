import pickle
import gzip
import wordfreq as wf

# store
with gzip.open('freq_en.pickle.gz', 'wb') as f:
    pickle.dump(wf.get_frequency_dict('en', wordlist='large'),
                f, protocol=2)  # Python 2.x compatible

# load
with gzip.open('freq_en.pickle.gz', 'rb') as f:
    freq_en = pickle.load(f)
    print(freq_en['the'])  # should be 0.03890451449942807
