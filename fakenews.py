# import packages
import streamlit as st

import numpy as np
import time

# external imports
from utils import make_predictions, scrape_bbc, scrape_politifact, scrape_21cpw

# set seed
np.random.seed(419)

    
if __name__ == "__main__":
    
    start = time.time() 
    st. set_page_config(layout="wide")
    
    # set heading on webpage
    st.title('Fake News Detector')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        text = st.text_area('Text to analyze', height=200)
    
        answer = st.button('Submit')


        if text==None:
            st.stop()
            

        if answer:
        # print prediction, ADD CONFIDENCE ON YOUR PREDICTION
            st.write(f'We predict your corpus as: {make_predictions(text)}')

            st.write(f'took {time.time() - start}s') 

    with col2:
        pass
        

    with col3:
        
        option_answer = st.button('fetch')

        # pass
        option = st.selectbox(
            'Scrape a site..',
            ('BBC NEWS', 'POLITIFACT', '21CPW' ))

        if option_answer:

            if option == 'BBC NEWS' :
                st.write('You selected:', option)

                bbc_corpus = scrape_bbc()

                st.markdown("""\n---\n""")


                st.write('Results:', bbc_corpus)

                # option = st.selectbox(
                #     'choose?',
                #     (bbc_corpus))

                # st.write('You selected:', option)
                st.stop()

            if option == 'POLITIFACT' :
                # GLOBAL_STATE =True
                st.write('You selected:', option)
                # option = ''

                # st.stop()
                politifact_corpus = scrape_politifact()
                # time.sleep(3)
                st.markdown("""\n---\n""")

                st.write('Results:', politifact_corpus)
                st.stop()

            if option == '21CPW' :
                # GLOBAL_STATE =True
                st.write('You selected:', option)
                # option = ''

                # st.stop()
                _21cpw_corpus = scrape_21cpw()
                # time.sleep(3)
                st.markdown("""\n---\n""")

                st.write('Results:', _21cpw_corpus)
                st.stop()
            

            # scrape_politifact
            # else:
            #     st.stop()

       

    # text area for news
    # text = st.text_area('Text to analyze', height=200)
    
    # answer = st.button('Submit')
    # # since streamlit keeps on run whether text is empty, stop running
    # if text == '':
    #     st.stop()
        
    # if st.button('Say hello'):
    #     st.write('Why hello there')
    # else:
    #  st.write('Goodbye')
   

    # if answer:
    # # print prediction, ADD CONFIDENCE ON YOUR PREDICTION
    #     st.write(f'We predict your corpus as: {make_predictions(text)}')

    #     st.write(f'took {time.time() - start}s') 
    # stop run
    st.stop()
    



#  text = st.text_area('Text to analyze', height=200)
    
#     answer = st.button('Submit')
#     # since streamlit keeps on run whether text is empty, stop running
#     if text == '':
#         st.stop()
        
#     # if st.button('Say hello'):
#     #     st.write('Why hello there')
#     # else:
#     #  st.write('Goodbye')
   

#     if answer:
#     # print prediction, ADD CONFIDENCE ON YOUR PREDICTION
#         st.write(f'We predict your corpus as: {make_predictions(text)}')

#         st.write(f'took {time.time() - start}s') 