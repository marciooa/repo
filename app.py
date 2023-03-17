import streamlit as st
import pandas as pd
import yfinance as yf 
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator
import streamlit_extras as ste






######################

st.set_page_config(layout="wide", page_title='QuantMind', page_icon='favicon.ico',)

st.image("logo.png", width=150)

with open("Style.css") as f:
	st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

##################### autenticacao
##################### autenticacao
def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():


##################################333
    df= pd.read_csv("tabela.csv")
    vale=df.loc[[0]]
    petr4=df.loc[[1]]
    itub4=df.loc[[2]]
    bbdc4=df.loc[[3]]
    b3sa3=df.loc[[4]]
    abev3=df.loc[[5]]
    jbss3=df.loc[[6]]
    bbas3=df.loc[[7]]
    suzb3=df.loc[[8]]
    ggbr4=df.loc[[9]]
    sbsp3=df.loc[[10]]
    mglu3=df.loc[[11]]
    csna3=df.loc[[12]]
    petr3=df.loc[[13]]
    mrfg3=df.loc[[14]]
    usim5=df.loc[[15]]
    viia3=df.loc[[16]]
    elet3=df.loc[[17]]
    ciel3=df.loc[[18]]
    wege3=df.loc[[19]]
    prio3=df.loc[[20]]
    elet6=df.loc[[21]]
    itsa4=df.loc[[22]]
    rent3=df.loc[[23]]
    eqtl3=df.loc[[24]]
    radl3=df.loc[[25]]
    rdor3=df.loc[[26]]
    bpac11=df.loc[[27]]
    bbse3=df.loc[[28]]
    rail3=df.loc[[29]]
    csan3=df.loc[[30]]
    lren3=df.loc[[31]]
    hype3=df.loc[[32]]
    vbbr3=df.loc[[33]]
    asai3=df.loc[[34]]
    cmig4=df.loc[[35]]
    tots3=df.loc[[36]]
    klbn11=df.loc[[37]]
    ntco3=df.loc[[38]]
    hapv3=df.loc[[39]]
    brfs3=df.loc[[40]]
    rrrp3=df.loc[[41]]
    mult3=df.loc[[42]]
    also3=df.loc[[43]]
    cyre3=df.loc[[44]]
    azul4=df.loc[[45]]
    petz3=df.loc[[46]]
    lwsa3=df.loc[[47]]
    cvcb3=df.loc[[48]]
    
    
    
    st.sidebar.header("IBrX50:")
    tabs= st.sidebar.selectbox('', ( 'VALE3', 'PETR4', 'ITUB4','BBDC4','B3SA3', 'ABEV3', 'JBSS3',  'BBAS3', 'SUZB3', 'GGBR4', 'SBSP3', 'MGLU3',
                                  'CSNA3', 'PETR3', 'MRFG3', 'USIM5', 'VIIA3', 	'ELET3', 	'CIEL3', 	'WEGE3', 	'PRIO3', 	'ELET6', 	
                                  'ITSA4', 	'RENT3', 	'EQTL3', 	'RADL3', 	'RDOR3', 	'BPAC11', 	'BBSE3', 	'RAIL3', 	'CSAN3', 	
                                  'LREN3', 	'HYPE3', 	'VBBR3', 	'ASAI3', 	'CMIG4', 	'TOTS3', 	'KLBN11', 	'NTCO3', 	'HAPV3', 	
                                  'BRFS3', 	'RRRP3', 	'MULT3', 	'ALSO3', 	'CYRE3', 	'AZUL4', 	'PETZ3', 	'LWSA3', 	'CVCB3'))
    
    
            
    import datetime
    today = datetime.date.today()
    before = today - datetime.timedelta(days=365)
    start_date =  before
    end_date = today    
    
    ste.style_metric_cards(background_color='#FFFFFF', border_size_px=1, border_color='#CCCCCC', 
                       border_left_color='#7030A0', border_radius_px=5, box_shadow=True)
    
    if tabs =='VALE3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAeCAMAAACxDwjlAAAAqFBMVEX///8Ak5rsuDMAiZEAjJNlZmoAkJf5+fn19fXS0tPu7u6bnJ6JioxrbG+6uruQkZOjpKaCvMDrtBwAkZ/2uijxuS1usrfn5+fCwsN7fH+wsLJgYWWBgoXD3d9Npasum6Kgys7l8PH9+fL569CQwsX34LTuwFPrsgXwxmrY6er126Wy1Nfz0o7tvEP88+Ifk5PdtUOqqmapt5BImpDGsFZ6oX6cqHAAhpZbiKRpAAAB6UlEQVRIiaWU62KiMBCFE3KRqyBeIKKotVtqddfd1nbf/802CVSTkFZgzw8DjvN5kswMAACsJyWEm8V2B/5bW4op5KIUlTbcw37/0JVVYngVRY9m+MdTlabVc0fcAUFFuBypwZc0dYTmTkdrE6rSKD20UI5T7TvCwAZqQkcT5aSnriywQwZtoqMc52dnFr9PrNNweaoUlFP96gEDG6rT6Pn3XGG99GGBnWENwumfWYObz157sdob5bS3y2zONbuce7J46VKTBqfn94+P9/Pfw/1sQ6OWNcmbXgull45WGqSLASzrRjlrM4gFRjYYHjqV1qjFQutrNAzk4jFPLOOwcTDO6odxIqTQFqY3PLkFl0SmxZF8iyLJBG4xrsNBxJWp3swDK5WYS4S1EVmKlzxiYfPtJ0x1JaWPNki10ZYQl1Nqfyz0iH8Hpo82pFerL0yF0pBH8sbiDcbiOMx1mjLa8Nb4J35cbpE3T/yQdNgqSQLvq41qByaVkTwn0mPEkiCUV/DdNgF4vDZCO7ZahTJlGQVxHLP4LuxztCFLtXrN5UcyMS9cAUs8Lg6L61VXPcOxtb0ZqykyKSuWos4IIUXBYXwlrJUhRtsX7Z1JY35Tm74vP4R4AUq1U0o6tL0tcvHg9rbouL7/G7v+Ady1HWoX6v8ZAAAAAElFTkSuQmCC')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(vale['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(vale['5 dias']))
        col3.metric(label="10 dias", value=(vale['10 dias']))
        col4.metric(label="20 dias", value=(vale['20 dias']))
        col5.metric(label="30 dias", value=(vale['30 dias']))
        col6.metric(label="60 dias", value=(vale['60 dias']))
        col7.metric(label="90 dias", value=(vale['90 dias']))
        col8.metric(label="% Probabilidade", value=(vale['% Probabilidade']))
        
        base=yf.download('VALE3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi) 
        
    elif tabs == 'PETR4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAPCAMAAAB5hdnbAAAAdVBMVEX///8AhT8AgjltqYD9xmH9txz+y3EAgjdYn3AAcQCsy7Xs8+4AeB3x9vIAeiSYwKQAfi+LuZkAdRXm7+ilx6/R4tZPm2lJmGTJ3c/a6N5fonX+0YX9tQ/+1ZG00b2fxKq/18Ywj1OAs5E/lV0ji0t3r4kAawAZ0ot+AAABYElEQVQ4ja2S246cMBBEC9jEd7ttYLDJBAbM5v8/MT1DpOw8s/VQEt32KasEfn28CZf0cf/xRfdvhN0vwn7/fNM12LdqWVf2EgK7Ces57LXWBYZ9QGbXprwmgI76XI/AoPWDR254+hiDwc1LPBZ0G/KC3Z6waKtQbrV1qiAir/jYJBScaKuNvJ4a5ca0bfyB2U5ASHuqkLQgBtQVUqKjE3Yc+EyYiFOYnAxgZ9w2VN5biU30t5mRfVYZDys3gMTAb5XWmcUZ1cNh8eLFMp6SWmCPup1kZLKJjEsRJQVnp86vOEj5HfBD5Fu5+pTBWF0LBIY/pdAJ0/bZz8OHwmk9E7Anp23u09xvgjPXzMi0Q1R0/mg81tkEVXCLzw73T0hf+n8w+aquI7It18yJoO3JQ5eUdJiJxA6dslNxVLrvEkavuC7uzLOE8G1DvhHXfg3ZNl90FSba/xJ0DRa7N11i/QWCBRofqBpCcgAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(itub4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(petr4['5 dias']))
        col3.metric(label="10 dias", value=(petr4['10 dias']))
        col4.metric(label="20 dias", value=(petr4['20 dias']))
        col5.metric(label="30 dias", value=(petr4['30 dias']))
        col6.metric(label="60 dias", value=(petr4['60 dias']))
        col7.metric(label="90 dias", value=(petr4['90 dias']))
        col8.metric(label="% Probabilidade", value=(petr4['% Probabilidade']))
        
        base=yf.download('PETR4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'ITUB4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAApVBMVEUaVJMYU5P/////+AAuXpj/8hL/+gAASZcGTpV7kHYATZYVUpT/9A3//wAAQpksW5CJmHAAR5gAQJoARJixtlvj3jPSzkWss10AR43CxE8APpvm6vAAQopshHyClXMjV5LMy0nz6iK7xthsh69ffarb1j2nr2Cbpmc3Yo3h2jhyiHqPnW5ceoJJbYhogH5Tcobp4ywAOZy5vVWVomqhq2R4kLVCap+p+URKAAAB50lEQVQ4je2VW3eiMBSFgyEXcqMQqYKKiQ4MVmvVafv/f9qcMNPRmVq1b/PQ/cIK51thczhkowFosYzRJUXxchE4NBhM4rG8yAItx2gS4Mk0uoL2ktMJwPObWNg9GqDF+DYWofECLa/5PRr5hi734Utf+h/ErbUw1cxadrYOBf6HrbXWqcward052jitW/EGJ5hQgO+VKs/AIqH0u0F/w3mATXgeF4wxEf5jyblIFX6uOJencJeslGqSBx6xWVu6cs05kpu6fhDWsLquH+URnm+1IkTRImOEYooxJU+cHSjdWThiKNZr8Q7WRZatdFE6ohRhbIhVEWBF8N0JnM478Oy6TsptWlX7yiua2I9gacMLZuBM5Fsw7Qlu8w/ht9axmQfTFOqjqzAH89gP1406wvw8nKGsgQ5WLD9ggEeY+ArJCP8LM6eUN9Z6hVsjqh3sbH5AJdnn5TtYPGPoV7NvoIV3yQrqI9ZpQvCO4FMbVMEgyRRjpYp8Q5WilBaYDll2gAV8KYfpb1huXOnSCPHOeX9g4unee/cIN2uO7LrwRWtnzs3C1MCRK2Fu+rFhxrBwyQ2TnLFQFpmxIvq1mH/uMP9UTAziG7eWKETb1RTsFfXRBqE5ldEVyXHch2aI45fX+KJeX/o4/glsbSlgN1s/qgAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(itub4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(itub4['5 dias']))
        col3.metric(label="10 dias", value=(itub4['10 dias']))
        col4.metric(label="20 dias", value=(itub4['20 dias']))
        col5.metric(label="30 dias", value=(itub4['30 dias']))
        col6.metric(label="60 dias", value=(itub4['60 dias']))
        col7.metric(label="90 dias", value=(itub4['90 dias']))
        col8.metric(label="% Probabilidade", value=(itub4['% Probabilidade']))
        
        base=yf.download('ITUB4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'BBDC4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAZCAMAAACsCjhdAAAAbFBMVEX////HAADJABPJABbgjpTgjJL029zdgIjRQFHhk5nNHTb34+TUT13twcTROkzvyMr89PTKAB/LACjlpKn67u7bd3/YZ3LLACTps7fZbnfjmJ7VWGXWX2nTSVrorbHSSVbPMkXy0tPOJj3MES8FtHXiAAABgUlEQVQ4je2T226jMBCG57cBY2xOwQ7gEMrh/d9xx4m67SpoFSmt1IvOhfkx428OHoh+7adYlwt5qb8E5QrkXTlM01fAdlnenqZ8nZUI6+11UrN5GVW+iSpN0jEHsLzatrrBcFfrCKRRpEd+2fAMrUH2Ltc26qs49DoM8WDyo7gOrPPTISx5CpZ+xEx7XvJ9WhSRSobK2aLqeEtXVZtQ43fLmatimXndloH0dvv82domhnZE8x5V3vsLzmRbcXZjuHBLLbwSCW2n+QpSSJNAV4yjUfBnhH9hznJ/UZvpHiWWmYMut16aTCgDxWXqDJ0rUSuwm8HIH8EHt/6hVK+xvusI8wyTfEYCvao5OQdd8gswNDxE9RqJjoPQhAfYGFB/hi13mGJPoTLomNmK+e5g9sLBx8z4B1zkf2FVP098d5YnJCAMwlMBHXg0dhm6kVQ39AtHS7XjhqmDkfFB/C1T7WLjIqY97rdRN2cp+e7cJIUl3YrcxC3RkZftc+P3a99tfwCfQxQn7dwBKwAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(bbdc4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(bbdc4['5 dias']))
        col3.metric(label="10 dias", value=(bbdc4['10 dias']))
        col4.metric(label="20 dias", value=(bbdc4['20 dias']))
        col5.metric(label="30 dias", value=(bbdc4['30 dias']))
        col6.metric(label="60 dias", value=(bbdc4['60 dias']))
        col7.metric(label="90 dias", value=(bbdc4['90 dias']))
        col8.metric(label="% Probabilidade", value=(bbdc4['% Probabilidade']))
        
        base=yf.download('BBDC4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'B3SA3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('https://ri.b3.com.br/wp-content/themes/mziq_b3_ri/img/logo.png')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(b3sa3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(b3sa3['5 dias']))
        col3.metric(label="10 dias", value=(b3sa3['10 dias']))
        col4.metric(label="20 dias", value=(b3sa3['20 dias']))
        col5.metric(label="30 dias", value=(b3sa3['30 dias']))
        col6.metric(label="60 dias", value=(b3sa3['60 dias']))
        col7.metric(label="90 dias", value=(b3sa3['90 dias']))
        col8.metric(label="% Probabilidade", value=(b3sa3['% Probabilidade']))
        
        base=yf.download('B3SA3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'ABEV3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAdCAMAAAA3m3pLAAAAgVBMVEX///8ARIwAP4oAQosAM4UAPYkAO4gAN4YAKoEAMYQAOYcAL4MALIIANYZac6TN0+H3+PoAJ4B5jLOptMzAx9nV2eXi5e3a3uhtgq3w8vZyhq+hrchkfKorUZKMmry5wNQhTJA+YJpPa6CXpcIACHkAD3oAHn4AFnsAAHUzWJaDk7gcKWTCAAADK0lEQVRIidWV29KbOAyAJRtzNiYcjCEGQmg3S97/AVcySacX7ebfvatmQgYjfbaOBvi9jABdB96CuM8AfUO/9l/UfyvWQivnCoyAbwCpZa4HmPUItXT9f0G1N99D58YNQJgDoFhWgHUCM00GzN1+B1iGr4Cu2MPqOwN23h1x5RPgr3Yf7bRAdctbuC7TDvCgIzr7gdXRQWD81pJff4OvoG4GjlxX120NE6wOqq6inQRAdXyKYOv5GT9vBrr6lxqm7g9oiXu/foLVjysFqPsUYtOPaVOsH7TALt0nlVNGmD7C/iwZjPmi71+QuYgev07t/5BNYPrnw/pm257jsCxPC/u+rPVy3ybqu6467jsr3AkGQ3Ns+9vkumXoKClktFx5od5J6H9KlRBxVOn80oNKkkPmQqjL2pRCCo11gImqVFIkeRgWFrWQUpXUuo88vvBSd8kjmgvPCFEqUkfMerhJlDJWiKhjGUvE3AUYCtZBmdEEqFlba8TE86fMEKyJUXdgL6SYTK7ANwz1MpEmink5yP7ygkWTyxBVBeBijO9mpcV0aBOMaUhBjLKgKRejuNObKd6whIZBo+iAtJpLLGxw86hPnXQcLyhpjMOQoWrqFCVS2AtU7ILELASiEhgZhhVspjFuzkX6SrDCvjKhu1WjevbGDFISlDJdWlhyjCgfN9rsTFB+wngj6CPMOTlOMYyQMujsOeZX8gVVRCLZlPxMrjBLqek7/oAlDJtlcMFEGDPM08nsT7AY85ZhItFBHlAXFKaxRDXB6WZwYVIv2HbC8uV0sxz5ebrp2U1yQbh1XWmYGxNUctok5PSpqIa4dkp8wfgW6PTpJpdrgJ06nIB6KM8EQLgRgUKIlK6E34cUKdHrriX+5CbBgpuvkynWaZeEzHzoLnGsZl3mB0+mjCwpr4HuEw5BLn/AbhBSHcqHSiTqGck6VMOSbmGwEcUwiaiqy+GMTzANci+4N7JDiZJgSglutVTEik+YCv2EivpLx9RcyVlFds4UbU69xm8mFfT53bVrhdtie+/8AJN3jtdaP7kQUud8vXjvRur+an/Pjq7ZbrN/XXXO+yp0+z9+4jgwRYr34wAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(abev3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(abev3['5 dias']))
        col3.metric(label="10 dias", value=(abev3['10 dias']))
        col4.metric(label="20 dias", value=(abev3['20 dias']))
        col5.metric(label="30 dias", value=(abev3['30 dias']))
        col6.metric(label="60 dias", value=(abev3['60 dias']))
        col7.metric(label="90 dias", value=(abev3['90 dias']))
        col8.metric(label="% Probabilidade", value=(abev3['% Probabilidade']))
        
        base=yf.download('ABEV3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'JBSS3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAArCAMAAADluJ77AAAAe1BMVEX////cAAClpqjeJhreIxfeHAzogHvzw8LeIBPmbGno6On6+vrxt7X43t3vrqu5urywsbP99fX55OTup6XtoqDiTUf209Lqiofx9PTfLiTOz9D97ezf3+D32Nbu4eDtnpvgQjvlYl3jV1LpkI3rl5TneXXCwsTgNS3U2NnN/i8TAAAB90lEQVRIie2U2YKqMAyGEwQrWLqBZR/ABXn/J5yy6HFYHM7V3PjfCM3fzySkBfjoo4/+WHKby882+ZT+1SdpsQnVSQfvcWGwGdXbo/WYPOn/YgEUiYLjcSnyhf74RGhYhmEZkMKnAWNBGDKi+oiWPqWUsUeBPhbHeIHlHdjLW+XgUEONGEkVIdYS/L08R10i5PTwMfxayCy+2K+v7s4Z2Hv7cDU/551zA4QAh/C/fuzceWZxbP/o5hRW2XiFWsuDO5mwaCG1VmK5ArP3BTknN2JeLgHQuv4xEiH6+RSWAq5ltrsR5jp12aUkKSVSn07+0xhhlk5hDbjJuzIjx8GxQHaBKz5nO6nM3ok4KKQ/YEheYQUmSMbmXBngdfRR1PEMljdmvZ8lvd+bIlwcv/4IuzlYQTXQ3ILg2DZlOs29KQx4C6SfWnJHLNl5SFORu23fy0t1d80CrQNiBlqTcqzYRwbpLDEjkUJ26s+mNBoXhwe5cuEEiQ8NXww1wgPibj+eRc3AE7NPOSq3eAyk3IbTFwoeF/N+PZVaIoeMaPULSRFz8Fsh2ve2XFi8jaXK5OLNYiQzpWTccovPJn+uzmc1rbd0s/RxLzUG3q792VTH3m8J3qRt7j2Ut2nDhVnn6ZtOrRHzbnO3e5Do4Lm3NaNV7vLV/NFHf6Jv3aEf4/0eJX4AAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(jbss3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(jbss3['5 dias']))
        col3.metric(label="10 dias", value=(jbss3['10 dias']))
        col4.metric(label="20 dias", value=(jbss3['20 dias']))
        col5.metric(label="30 dias", value=(jbss3['30 dias']))
        col6.metric(label="60 dias", value=(jbss3['60 dias']))
        col7.metric(label="90 dias", value=(jbss3['90 dias']))
        col8.metric(label="% Probabilidade", value=(jbss3['% Probabilidade']))
        
        base=yf.download('JBSS3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'BBAS3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAABECAMAAAAPzWOAAAAAq1BMVEX9/DJGXvz9/DH9/Db//xhDXP7//ydFXf0+WP87Vv8zUP///iz//wA3Uv8zTv9BWv/u70zy8kOMmMePnL6Tn7yNmcTe4WXM0H7X22/29jvh5GDLz4JseuKDkM7V13NJXfS4v51xgNxPY/NhcumjrLFUbOxTafCYo7eEk8oqSP/S1Hi8xYqdp7Wpsqe/xZLb32x6htYhQf+mrqvFy4iwuKLn6VVldeO5wJV8i9K7vS+jAAADL0lEQVRYhe2W2XaiQBRFpbxcqAHQOBMTYzTGIcbEiOb/v6xrIioC0unVb9YTuqo2506nqNVJ7R8XqddukBvkBvlPEMTLY/zvIAR695DZwqF/SrkKQeww1jkTQ6A5fIDqEAKPI+o4dPR4FMPhKQjuqkMQW6HryOWGLSuGQGPMPL8yRMp4po5d9HmjxBApI3KcypBUBvWpEdNGJIMJ8+SPiuEQ6GsZLpvC1MSkxGBv5Ete5+xQEQSxrU8GL10g0J0FWgx7BajPF6Plec3zIQQ2JhvhK6h8cnw1YoJZF6BXx/MjuRDkbRvASpBzqrt4w2zr5UFkNmZpUegadGtygLTaKsCrEAQrXa9gEnOJjSfvQvRHtkxTwHIIbo69oRab1RG3iyj8GICcAEOexVgG4ZtP/wThhluQMlRt/MUGRc+8gLKkdAAxmQTeT5u+xCC2OrqIrhAeZ+rRk6quWAGHtWpsdU4GL+IXJcNjMhre0Tg/+hJXSyxHbMh0GWIB61ABI/8gbAd77HuQNancPuGwC30lI9kbGeMmQJtpGXQFPLu/qGMbHzFIlJYRPAnYzKiNCnO2F8yO7K5krwvKxg3AN5uNd3Ehowwidjq9EdudJFdGVR2icqvnNtgnAFOdjSg4CLGUsiqGw419SRlrAckkTa4gnVApq5RYaI6NfU1kck3TRFTK0GbpsWFyfQC5OOhzas6gkdZYJrdj5zIKsmIu297KcKUMflJjO8KOZu6T8gHsLswA0qXAZejbGqculc7UIi4fQPtKj7UQmh9hFD4BH0TBqT0Ek3Il5t605t4X4jBUNUXjBmapml3JycmdJW8abrqLyNFOU6Jap1bFqGu2ElSau3VqsaPGHtaV+oSA7NJl6qdv2k+RzHWtZTYqdSwOvj/VtXDHjmIs0w1yZORB4N7zlR8h9BxdbJdtSSv0bDbyr9wMRN67en/YIDIE/exR6hdlowBy56tMzOtcf2g5P9ZfKCMP0vHld1HPOjHWH7QY1RtFMnIhNJyTn34kcO/6ukULZeRCvKUgx3+IEqOKUvZ1mIXgV/ZCILCKswZyBUIuzZxgcTbyIb9aN8gNcoP8FvIH1x48/eb01S4AAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(bbas3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(bbas3['5 dias']))
        col3.metric(label="10 dias", value=(bbas3['10 dias']))
        col4.metric(label="20 dias", value=(bbas3['20 dias']))
        col5.metric(label="30 dias", value=(bbas3['30 dias']))
        col6.metric(label="60 dias", value=(bbas3['60 dias']))
        col7.metric(label="90 dias", value=(bbas3['90 dias']))
        col8.metric(label="% Probabilidade", value=(bbas3['% Probabilidade']))
        
        base=yf.download('BBAS3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'SUZB3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,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')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(suzb3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(suzb3['5 dias']))
        col3.metric(label="10 dias", value=(suzb3['10 dias']))
        col4.metric(label="20 dias", value=(suzb3['20 dias']))
        col5.metric(label="30 dias", value=(suzb3['30 dias']))
        col6.metric(label="60 dias", value=(suzb3['60 dias']))
        col7.metric(label="90 dias", value=(suzb3['90 dias']))
        col8.metric(label="% Probabilidade", value=(suzb3['% Probabilidade']))
        
        base=yf.download('SUZB3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'GGBR4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAABECAMAAAAPzWOAAAAAzFBMVEX/zAH/zAABPnT/zgD/////0gDhuyAALXc4UWVeal4AL3T6yg0AOXb/0AAAPHX/1AAcR2z/2gAAL2wANnjbuSaLgk0AKmoAJ3rpwBLKqzIAKnkANnAAI2gAJ2kAHGJDWGQAHX3QsiSDgFM5T2vlwR5RYWFBX4csUX26w8/m6+5TbY9mfZutusfV3eKjrr7v8fBxhqHGzdUlTH1+kqkAFGGSoLEiSGUABH8AF30RQW1xcVu1oTvEpzunkk+AfFZib1unlEaqmj+bkEiTjE5qY2k2AAACvUlEQVRYhe2Va3eaMBjHhQSjMSGQIFcVUbygVmvXdaKds+33/057rLrTU+k5w5cbfw7kQvgleS6kVqtUqVKlr6ShQmmlICitFygtRdGEFZIreSNRCmI0TP1KrFlB/jmIeUadypsgUh9PZKTrkZyMdfc2SDTFGGczKecZVBbyFkjnDmdL4MzmGE+XK7zulofIe7zuye4YL6b4wZWAnMnSkC58a5puR+/19K5rmkCjpSEwddccr9fT5WI6XT+YOl53SkPcBR7L2dG0K3hM5Bwvy68kGuPsoff4Dd9leP7YG6/w5AbvuMvTKrLsdH+Xt8SJe5/h1XI5BatgfDd3b4vYqNvrSOm6UnY63eiGiH0i9ErhyCj1u9dahSp3ZBQfPH/D0LTTMO2jLs3a5c35+afv09yC+xx2fZr1iEQaF0cuQoZA5+XxMwfa1yvTRBKHHm0bSEQe6Ic/6HseiVMebMKQxg6HIVHYDzhKNpsW8jcbB32G8MBjKgcPcGGZ1nCY+22VxzrLRUB1kzLiwNeEsa2AggKE0iuIJnLW8I1d4xkJS/20hTDadGTXFUkDEvl+gz0JY09/MdXiCSHFEMATx4BD20mFxUaD/bM4Q3yAtIxnGqY8J05MXowvITygyhdWP/T2tmUqr78XsJ0GowPxDjnOEZDcPtDY/gqiHTeaiMMhVgPbUgMnSQ2AKPUi0BEidspr7ZXV3jKaOmAT7lNSYBOLDX07Md8hP4VhgE2aW6W3eEDMJLBYLJhJw5CpV99T7fqegXU/ewfVqSI6jAEIU4Rs/DYZ8UiNYDsmIYqlQUiSxNlSy25CHikyENfBxv2tbm5frDc7Hg6PLn61mvbOyncJODwe+GJvNQXiSZ47/C0ejg6F2YgMzg24NONdCKo1DiU6NTWoQ7SjSw8vzqRLtmgFOr2ufUifQkSlSpX+Y/0GwZVJ8JtY01AAAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(ggbr4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(ggbr4['5 dias']))
        col3.metric(label="10 dias", value=(ggbr4['10 dias']))
        col4.metric(label="20 dias", value=(ggbr4['20 dias']))
        col5.metric(label="30 dias", value=(ggbr4['30 dias']))
        col6.metric(label="60 dias", value=(ggbr4['60 dias']))
        col7.metric(label="90 dias", value=(ggbr4['90 dias']))
        col8.metric(label="% Probabilidade", value=(ggbr4['% Probabilidade']))
        
        base=yf.download('GGBR4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'SBSP3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAA6CAMAAAD81Uu1AAAAilBMVEX///8Ant4Al9wAmt0AnN0AAADd7vlUseTE4vSMyOsAldtWVlbZ2dnq9fvv9/yrq6vQ0ND4+Pi+vr7l5eVvu+f2+/6j0u9CrOIvpuCzs7M0NDSCgoI9PT1LS0t1dXVlZWWcnJyKioq73fMAkNrR5/aw2PF9wenu7u5EREQeHh6Tk5MsLCwMDAwVFRXBYe/AAAACXUlEQVRIic2U25aqMAyG0xNIqXIQEAYFZFC2OvP+r7eLQFsQdc3NrPkvutrwkSZpWoA/o/XZ0Zp+surEcZLaMiycKGGDbCKKByuxNyOMkRJV6CrFlEoDIXJE3HoBb2zcMZTbThIRgvALuLmjaNzdwS/gmt8XJBpjOn0+hQeWIp1s9Ay2ehaRk1Gx5gmc0n7O12bFl2GHDHOz5hAvwrFa8Q08agorx4is3sKIqvnuHWwu8Ok1jBJiLHDyEk4jikw6nTufeE4ncNd05/VTmD6I8F39JEF7STu7XoSterWkejyg9aTOjf3JMZlLtehm1kgbh+JpmrIsKksyhaVO6QzXTbWjc1herNQ8HZoqWPeOcbvBPB6q35OGL8FgnA9utNnoNAOu1YbmbQTdPSYc686eNJRyTSfW0TixwmqMmpjW0QOvJzBEw5bYeDDHwyI2zDSkbtRozMSoscpmCFu7HlqGovgBhrg/MkoHet3/TdIFtoub96/s2YrBcoYnN1pEpVaoJzDnwwQtPR2j6pQTSvtwCH+4rXOtkyilGNM0Sqw36J/RIfsB/OG9I7Z+IEfRjR9Z6/embhTi/l20ms33OfNh/y9nWzm6l72Mxi26RVmwwGfugYUKllM/DOT+hwr2Rbf2XIBrGbAWPCHkXxVTcMZY2UJ+K9yrDAPArfKvy+XmQs7YEYQEt2wMRPpsyzKUtg4+Ss9ZVXZhb0MQF0+wAHzt+bsI95Vg2fUrh9v30WUQsMJjXsCqkPmCuR676gyzSiYgKtEKmXjoBXeTLETryVF6rnR+b2SE8F7b/Afwb+g/5CAiJ92ien0AAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(sbsp3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(sbsp3['5 dias']))
        col3.metric(label="10 dias", value=(sbsp3['10 dias']))
        col4.metric(label="20 dias", value=(sbsp3['20 dias']))
        col5.metric(label="30 dias", value=(sbsp3['30 dias']))
        col6.metric(label="60 dias", value=(sbsp3['60 dias']))
        col7.metric(label="90 dias", value=(sbsp3['90 dias']))
        col8.metric(label="% Probabilidade", value=(sbsp3['% Probabilidade']))
        
        base=yf.download('SBSP3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'MGLU3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAB4ATAMBEQACEQEDEQH/xAAZAAADAQEBAAAAAAAAAAAAAAAAAwUEBgH/xAAvEAABAwMCBAQFBQEAAAAAAAABAgMEAAUREiETFDFRBiJBYUJxgZGhMmKx0fAV/8QAGgEAAgMBAQAAAAAAAAAAAAAAAAIBBAUDBv/EACsRAAEEAQMCBAYDAAAAAAAAAAEAAgMRBBIhMQUTMkFhkQYiUYGSwRQWof/aAAwDAQACEQMRAD8Ax179eGTVxn0RkSlsuJjuEpQ6U+VRHUA/Q0gkYXlgO48k5jcGh5Gx80zkJmthHKP65CdTKdBy4O470vfionUNufRT2ZLA0nfj1TJVpuUNDi5UGQ0hvBWtSDpGTgb/ADpWZUEhAY8ElM/HmjBLmkAJgsV3KG1C2SiHP0YaO+2aX+Zj2RrG3qm/iT0DoO6VGtdwlMLfjQpDrSMhS0Nkjbr86d+TDG4Nc4ApWY8r26mtJC8ets+Oh1b8N9tDWniKUggIz0z88ihuRE8gNcDfCh0ErQS5pFJXLSOV5rgucvr0cXT5dXbNP3Ga9F7/AES9t+jXW31Q/GfjhovsuNh1AW2VpxrSfUe1DJGPvSbrlDo3MouFXwk06RFCF3UedaWPC9ot13GqM+2t1RR5lIWlYUNhuM5Irz74sh+VJLD4gQPsRS3GSwMxo45eCL+92qrV2izJFsllxmM9JhvtMEqGGlFSdIPbYH+PWqrsaSNsjKJDS0n15tWhkMe5j7okED04pYWC/avD0tq+3BuU4iUw6WuPxVJRxEZ6774JxXZ+ifIacdmkEEcVvRXBuqHHcJ3WQQeb2sKjbhId8WKmovbD8CQg8GOh8qJGB8HQY7/3VeYsbiCMxEOHJr9qxEHnKLxIC08C/wBKWrmZ9otLlmujURmGCJYL/D0KBGVKHqOvXv71aGiKaQTsLi7ja/ZVjrkijML6Ded6W68li6/9y2R5kZMh4MLb4jgCVAYJ3+n5FcMfVB2pnNNC13yNMwkha4WaUpm0Ou+GZViRJiGcxKDxHF8pSQNwfv8AarjsprcpuSWnSRXHmqrcZxxnY9jUDfKn+N+ElNmZafafDMIIK2lAg4wM/irHS7PdcRVu81X6jQETQboLmK1VmIoQt5s8xLKHihAQ4kKB1joa87N8VdMhldE95tpIPynkLZx+g5s7A+Noo78hYVtlCiFac+tPH8TdNkNNcfYq634Q6qdw0fkEsrbR107e1aUXUIJh8pKb+m9W50N/IK6547U004IsO3xJDqdK5DDBSsj2/wAa4s6Yx5Gp7nAeRKtSdH6tGDUTGk+YIXNtzYzhwg5I/bWwYnjlYMvRsuLxNHuFrabLo8iQa4l2nlZkrO1408QXj8CfuKpTdSx4fGf8VfvxpbzC2FALSASM7Gmw8+DMa50JujXFLqx7XcJdXEyKEIwOwqUUjA7VCigjA7VKKCMDtQigjAqEUEYFClGB2FCEYA6UIRQhf//Z')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(mglu3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(mglu3['5 dias']))
        col3.metric(label="10 dias", value=(mglu3['10 dias']))
        col4.metric(label="20 dias", value=(mglu3['20 dias']))
        col5.metric(label="30 dias", value=(mglu3['30 dias']))
        col6.metric(label="60 dias", value=(mglu3['60 dias']))
        col7.metric(label="90 dias", value=(mglu3['90 dias']))
        col8.metric(label="% Probabilidade", value=(mglu3['% Probabilidade']))
        
        base=yf.download('MGLU3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'CSNA3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAbCAMAAADhwplWAAAA1VBMVEXv7+7u7u3x8fAAAAD08vD19fShudIAmTz31DT20y7O180Aeb8Ad7u30bLr7u6zs7LY2NcAWabKysng4N+5ubjm5uXBwcB8nsUAXKcAVKOJiYj///9ok7/59/KgoJ8AT6JQUFBZWVlRg7Tw46yRkZCnz7Gzw9XH1OHU3ucmcLA5ebRIfrOOrMxBQUE1NTV0dHRkZGNMk8WzzOAnJyd3qtBoos2Uutbw6tPw5rvw6Mny3ovx23bx4aHs1Xzn5NXy4Je51MCYx6SBv5JSrm9mtn7L4NDb5t1iH2pBAAACs0lEQVRIie1TbXvaIBQNEOzabgEhoIkGaxObtPNtrtV2azfNqv//J+1Cspq13R6fZ/uwDzsYCBAPh3vP9Y7evTk+OX0beH8KhJD3n+wn+BWqCfZfweFkQcfhwrHhvPUKvEPJkk7bohspXMmkSUJBDaV2cK8HK/OLqNsHYZfdfuIWKDeGUzcIipimWDN8IFly1X6fgII8GuT2otQQQNxjblCECHpG6EFkOAhanQLbl/E4DwKMOZkgNCXyjMjebA5k096wSYbx03+fy+pH7W632/b9TmTHgQJhIcUYWYGTzFNkSNi8ScY5bFt4RdMElux8AGztCPudAXBFA1mRKa56PJ4SIkkWk8Y1TznjITTNw+BDvigg03s2VKgLuB4oVq1WXigfrnlG6ZSoj9Neb04EiSnEbk8mjQhDxkIjg+X1zXJ8vZT76+Lksn1uE1BEgwsf1mlcJQCGKZkoMuuZPdnNjeSKhUyEQuHrxTJfLHL1zBqd8Xh81T2vrSGyWIM1dBaDJYzA2JjaGisIWA3InE9XGDdiViWhNm3h1q1bKUgFu9qBWuMmtWlXBoIFTYYqTdNVent3+9weQd+h5YT5vy6n4+NVJmy8QsPxp0/36eeH+/sXvkscar2v1XlVTg8PXwSqAiZxmt7df03Tl2S/BargHa11SJ+A7c+6zYeouQ60NPxsywC7Oa7d7SZ7MiO1YJoJoxjjOtSMrzfrzags1+Wo3JQIc/HjLC4xlVpCTyFlClGKuHTvUGIVGWeGCRYKan3GwCLb8tumHG0fR4/rx82OxjqeQYtn2WyWMRZn8xiQwZwNvQmsZbARD8Ea5QnHWthkSqoFFxxpuR3tRtvdbr2BbgRnwraEwwTn8EioEi4Uk4bBBoIlC641ZNNGANdV2ej3qKJkg/kE6h630vgayP4e0D9M9h2fckuLbCQBAQAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(csna3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(csna3['5 dias']))
        col3.metric(label="10 dias", value=(csna3['10 dias']))
        col4.metric(label="20 dias", value=(csna3['20 dias']))
        col5.metric(label="30 dias", value=(csna3['30 dias']))
        col6.metric(label="60 dias", value=(csna3['60 dias']))
        col7.metric(label="90 dias", value=(csna3['90 dias']))
        col8.metric(label="% Probabilidade", value=(csna3['% Probabilidade']))
        
        base=yf.download('CSNA3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'PETR3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAPCAMAAAB5hdnbAAAAdVBMVEX///8AhT8AgjltqYD9xmH9txz+y3EAgjdYn3AAcQCsy7Xs8+4AeB3x9vIAeiSYwKQAfi+LuZkAdRXm7+ilx6/R4tZPm2lJmGTJ3c/a6N5fonX+0YX9tQ/+1ZG00b2fxKq/18Ywj1OAs5E/lV0ji0t3r4kAawAZ0ot+AAABYElEQVQ4ja2S246cMBBEC9jEd7ttYLDJBAbM5v8/MT1DpOw8s/VQEt32KasEfn28CZf0cf/xRfdvhN0vwn7/fNM12LdqWVf2EgK7Ces57LXWBYZ9QGbXprwmgI76XI/AoPWDR254+hiDwc1LPBZ0G/KC3Z6waKtQbrV1qiAir/jYJBScaKuNvJ4a5ca0bfyB2U5ASHuqkLQgBtQVUqKjE3Yc+EyYiFOYnAxgZ9w2VN5biU30t5mRfVYZDys3gMTAb5XWmcUZ1cNh8eLFMp6SWmCPup1kZLKJjEsRJQVnp86vOEj5HfBD5Fu5+pTBWF0LBIY/pdAJ0/bZz8OHwmk9E7Anp23u09xvgjPXzMi0Q1R0/mg81tkEVXCLzw73T0hf+n8w+aquI7It18yJoO3JQ5eUdJiJxA6dslNxVLrvEkavuC7uzLOE8G1DvhHXfg3ZNl90FSba/xJ0DRa7N11i/QWCBRofqBpCcgAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(petr3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(petr3['5 dias']))
        col3.metric(label="10 dias", value=(petr3['10 dias']))
        col4.metric(label="20 dias", value=(petr3['20 dias']))
        col5.metric(label="30 dias", value=(petr3['30 dias']))
        col6.metric(label="60 dias", value=(petr3['60 dias']))
        col7.metric(label="90 dias", value=(petr3['90 dias']))
        col8.metric(label="% Probabilidade", value=(petr3['% Probabilidade']))
        
        base=yf.download('PETR3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'MRFG3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAUCAMAAAAQlCuDAAAAt1BMVEX///8AAEoAAEYzO2wAAEgAAFEAogDm6O0AAFQAAEwAAEP5+vwAnQAAAE46Qm9uc5HU1t6WmK0ADFYAAEANHl0RIl8rNWnX7Nd/g525u8ixs8IAADvJy9Xt7vEAGVpVW38qqSpFTHaIi6MgLGRna432/Pbk4uxIsUjGwtRWuFQAEj2eoLNxwHEAUkVgYogAWjbo+uZmu2ai0aQvMm05rDm53rmHyIcAACwAE1l7w3vm8+aQy5AAADZ2O1w5AAACPUlEQVQ4ja2UDXObMAyGZWLzYWw+gxMohpJQti5ZtnbtlnX9/79rEoS2d9ndds3EHciy/divpANgtHrTbk1/s4LLrS4CP8syZ1AfhktZa34UrOgi9vHW/VReyAqEv7PkhXv3s3MRreTiMPt794vPJm6ShFPMJsn5JltVdp5+Gxei/3p38u/U/TfRk+ddsWJazNn2jFXnTq4nlz+/oZXBFm4fToMHdW8ZpzM91oiYQlF2XJzBlnpXn9LRZvY1Hjs1Xug0UOoRNrwaYUvNcf1Gn2DDa51DkMsXdzJvSkrUAHxXU4OtFDqeXE+wKtBhzXWlEVYJmTdl3oNxStEAb3RepldV9CM0VxYGI6WsCh+OKOZR/Rxhe6VuMInxCPOh1W3By4EtoJYsTiOOM1HmbHuEdYt6J7QfhQvHhlp3aZ8fC1imAE9KPY0Xc6/xs5hh0GQ6hgRhXUDSW4KJDYpzqDipjmi1E+4CqtlOFNAhDK5d1LdyXfULB9t0hg0SFRJMBGOtGMK4RzDKWTomF2Exryl9WP6UqPfKpccdLyiTGQbUywTzWfgCs+cwRpW1CPNyOtQdTe3RTQS8wMgI1uoN7RN/hlVsgWfFPmrvqyldZGPjjA3kOWKGOQb1BuYgBMEkyZQNwSTtNNKCCYJIiCXCwo4krFylHm5obzw1jolmmGnx1XHeD2YNB0M3Mx3lwNCxLQU2W3HwsuK1e1fv/pnZxI4FMO8FvLX6eYm0OFj/Dxh0jBea+fbvK//FqrhrdyH8BhswKbzALvNhAAAAAElFTkSuQmCC')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(mrfg3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(mrfg3['5 dias']))
        col3.metric(label="10 dias", value=(mrfg3['10 dias']))
        col4.metric(label="20 dias", value=(mrfg3['20 dias']))
        col5.metric(label="30 dias", value=(mrfg3['30 dias']))
        col6.metric(label="60 dias", value=(mrfg3['60 dias']))
        col7.metric(label="90 dias", value=(mrfg3['90 dias']))
        col8.metric(label="% Probabilidade", value=(mrfg3['% Probabilidade']))
        
        base=yf.download('MRFG3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
          
    elif tabs == 'USIM5':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAVCAMAAADbyPgmAAAAk1BMVEX///8AAAD2hxL2gQD7zq/3nFP2hQj2hQD1fgD1fACJiIj+8enr6+v4oFeFhITo5+fz8/O1tLRubW2ura2cm5vNzc35+flYVlbe3t5fXV1zcnISCw0KAABJR0eop6eTkpL82L/5t4f96t74o2H4qGn94c/CwsJnZWU/PD02MzQsKSobFxgmIiN8e3v6wJj3l0X5r3mbwFimAAABv0lEQVQ4jaXT63KiQBAF4NMD4SbhKiAoEm8DyhLz/k+3PRMl1tZaVKT/nWH4pnsKgFfrYze18IsyXWP/mA/u2wzMsJzFTzwa1ixMGMcxnVwxExPumHbGfGyc891W2NYDokAC2ySRiIMI0uOEIMh1CvTzDPC9Rr0lq7YZMecfrCDeRw06qs8BAvIxUAesiFacQhClCCnmw9QKlnSp+6dYqbGlT5VaU1i7pohfogyewvrNN1aXtAQu9DjmEwy0jm9YV5FEXTGgMW/NJ8WISHY1eBAefxLLNnRZaazflhVI0vYba1JaMRYTGu44qtXcU5i6lF5jlKaUESu3zrBpGUs2xVlNi+yi7u7/2MDHSb0LNSksJxlSzb0NdyylTQyqh4ES5OpQ+QzLiM5EOagsqFRYyDffs66TxvCH4kwJfFrdtWr3HRv/zqulP1rZFoMPDEXBs6ZJFLYhf3MRhoaTj4SblkkmExbixE9LvZvrgzHDvGOOEPbPz/XrWrhCWOIWdkr+fB3D1Vaauc8XpwNbD//WC7Xn1oRlOK5rMCuMrxkW35qrkFs5h1kW9/bGTVmWZRuObU5vn6qF+fV+vR4/Tzr9BdpFH+65tQ5KAAAAAElFTkSuQmCC')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(usim5['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(usim5['5 dias']))
        col3.metric(label="10 dias", value=(usim5['10 dias']))
        col4.metric(label="20 dias", value=(usim5['20 dias']))
        col5.metric(label="30 dias", value=(usim5['30 dias']))
        col6.metric(label="60 dias", value=(usim5['60 dias']))
        col7.metric(label="90 dias", value=(usim5['90 dias']))
        col8.metric(label="% Probabilidade", value=(usim5['% Probabilidade']))
        
        base=yf.download('USIM5.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'VIIA3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,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')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(viia3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(viia3['5 dias']))
        col3.metric(label="10 dias", value=(viia3['10 dias']))
        col4.metric(label="20 dias", value=(viia3['20 dias']))
        col5.metric(label="30 dias", value=(viia3['30 dias']))
        col6.metric(label="60 dias", value=(viia3['60 dias']))
        col7.metric(label="90 dias", value=(viia3['90 dias']))
        col8.metric(label="% Probabilidade", value=(viia3['% Probabilidade']))
        
        base=yf.download('VIIA3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'ELET3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAzCAMAAAAKPR4NAAAAxlBMVEX///9Gs0FEebbZ5DUwb7H3+fzi6fLq7/YfZ64WZKzz9vr7/P05c7Ozxd7c5O/J1eefttVEdbxQgLq6yuDAz+P+/vbz97nt8p/p8Ize6FHh5zRGtjWpvtp3msaGpcwJYKvT3esAWKf6+9z3+sru86b4+9Tm7nj7/Ofi6mTw9K/s8pbX4hjb5kPk7G2t0yKZ0p5ywD8qrCmw267H3TjN6MyTyzuW0JOgzzvq9um8z7/e8N4zbblDmIJOh71DnHZakMFEiZ5Fg6kfILffAAACrUlEQVRIie3UbXeTMBQA4BBC3ggJA/ZaAnSb09lOne86u87//6e8Sehx81TnKfEcP+x+KYTw9N7kEoSe4l/FfkTr9CwatX92EA0D6/wyFvbs4PDoMBYG1sVFJOs5WC+WkbbzDKzjNNIOXIK1TK/iYC+vwEoXp1EwWLAUYhkFuzp2VrqIsqEXPrE0ffU6AnYUrJM312+nY+cLj71Lkuv3k7HTRUgsSZLZ9NZ1a3byIXHYx8nY5SI9+ZT4uJ6MoWXIy2GfJ2NfZskG+7qbICnLc5RT0+Gbb7OJmdGmtCtMiFIY791utN0slJu2s6sK+9gLuc12/ghkU3brEcN7d4njdu8zVpd2vRo1pW5nuy6/j3y4p+Gb7xO/ply3oCmlCK+KaVQINhRtYVgM6im2BhsDyS7788zm8R3lXLiYo6K/j8ktM8tHMWKpdoEK/hPL1JYsyF9g3XgRMKk1JMV4jXLoWjiK4IcOOvNYpjXcjsPM1Mb/PTyWW7HSlVwiSYiYG9Ov+rmWVc97Dpmqqu97YpAfHoY5UYJQxDA8nutgqHXRtq0MmBGFA5nk5TBkhnSaIqsoyjvBAKM5rQgauNU0c6sqsUWdYvAZjwkpXFUVDHisI65S0UgoEwHNNqkzUYc1azgdBPVvwlHcVchWv1szq9wJwdsNBm9lonUvwlZ6TIthEK4oXYme4woVAttSb8WwaSDoA6x8iJmAVStoTpcWnFSYm1+wWshQJgq7OWJhgtyUCWMey/xdN9aoRoRYRl0g2tcwFWrKKEztoAECZt2ClnDpVQsb4DNTNmDSddKmBTkZvwBke4Y6QRTHcA3DhZk7jMGAcrUqTuCYbJDxjVAKVSm+QmWvMCfjgUfHcCW426YeXAsOtZGZb1HY+Lrxkym0KTzLdOhVmMnccQyjOfqf4weVRTQWIZ2D6gAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(elet3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(elet3['5 dias']))
        col3.metric(label="10 dias", value=(elet3['10 dias']))
        col4.metric(label="20 dias", value=(elet3['20 dias']))
        col5.metric(label="30 dias", value=(elet3['30 dias']))
        col6.metric(label="60 dias", value=(elet3['60 dias']))
        col7.metric(label="90 dias", value=(elet3['90 dias']))
        col8.metric(label="% Probabilidade", value=(elet3['% Probabilidade']))
        
        base=yf.download('ELET3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'CIEL3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAZCAMAAACsCjhdAAAAilBMVEX///9ZY21YYmwAre9PWmXIy89MV2Pj5OVqc3zHyszX2txWYGv29/fn6eqJkJdSXWjw8fIAqe51fYVibHUAsO+5vcHw+v73/f/N0NKr4fmus7fa9P2epKm75PmSmJ5Yx/R50vae2fc7ufHQ7/xuy/VHiKVbhZocquJ/zvVNv/LE6vuMscV/ho1ckKprFUnrAAACkElEQVQ4jZWV7XqjIBCFHTTxY1QISKqG2MZ2u23Wvf/b2yEoktY8z3Z+JRx9mY8DRtFGnJ7jl+OWYCPV1SNpK54+DvHh8kCscC/FD2DH5/gxbAeQpD9J7dzE4+tj2P5HsOjUPWzZf8FEm+u8WLoRdEUUWuetX7iDHc/dpTufvqAqIxUgZLK3/0oj9YLqp4wEJY34Bju+jE0TN834FuJKDZy54GoXRS3jmXthh17A/Ausa+IlmsuTh5kEgIOUGUPATER5wrLCChoZpSUnSTLDvgxhHUEO8TiON+bHwtLESkyRVmlb7xO5wlpFrPomDMAY5AGs/TXGh7fz6+l0fbPYzrHSjDFsZ3Br6MkZJiQC6HLeEYAp4WGkvf/u5uLORBtd3wwytbBczDDKmOl1kQMfPKxH4KtGxnSFppKhKbdgGWIdrNa06QIT9Kde/fP0EcefNrVCMTvBDVhCDROVj4GKFjMszRB08AZNtrm6N2W6BSv2QMGWsL89jDJw857jdYzj8wwTmzAaMmAQnPfRA9iVRmthLcNsMzNBmak6CLNao1B4N7Rr4zIrMnZX/tozcrCJyiAiD7NT64M3LuQN2zMaDE7VFmzgoL7dqrM1yE9BnbZlz7eLhuzIh8UbZbXC6ACw2tOqO1irgHtviD9UpbtNrdHZ4NpW1Pa+mGGl4YCT278Y3IXijxOlzWctrfFv8zmfhkpRd6Du234C5MFBryY63zD12glFCIsk7QSTyc2kkOG7v4VSewiRJ5wBsxXv+NyQqqYlJ0DiqvLfADExp1FdTAY+qYy9twiYKC3s0d9Prh+iV/xm1wSMa9r6dSItQWtFvmi+730tQQ3aPVfka9/1pMhu68ey6L0rha4z0vplEP8AkBYsvb3UO18AAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(ciel3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(ciel3['5 dias']))
        col3.metric(label="10 dias", value=(ciel3['10 dias']))
        col4.metric(label="20 dias", value=(ciel3['20 dias']))
        col5.metric(label="30 dias", value=(ciel3['30 dias']))
        col6.metric(label="60 dias", value=(ciel3['60 dias']))
        col7.metric(label="90 dias", value=(ciel3['90 dias']))
        col8.metric(label="% Probabilidade", value=(ciel3['% Probabilidade']))
        
        base=yf.download('CIEL3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'WEGE3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAA1CAMAAADcZP0QAAAAWlBMVEX///8AZKYAYqUAY6YAVqBJfrMfbaoDYKTt8vcAXaPd5O4AW6Iucq02c62qvtfS3OmRrs5wl8BdirnCz+GIpskaaKjk6/MAR5kATpyhudT2+PtlkLx6ncTI1OQQT6aFAAABLUlEQVRIie2X23KCMBRFIQmGi1SKoAj6/79ZsqOQS+tIOA+tZT3t2ROXDJ5IiGJCon8lYyRoGd+RABkrIxog22+yQFmfK1LkFLlHzl1OxhITU3Y4CyG6BrnpxnzOkVth0w2oL53TC0smxpxVyFU2ZqFlJbMHXX6i/ii+3QF/XJYppCeT6JfKGsVVOjI5oN8vk7V6HIQjK27ItQyQnTzZ8R1l/j0LkfH2okC9/sp4Ng3UetkPO+DdZLyYEMPqX/M4c6CZM5NNNpKHyLz/sziuFYlqWIkMgTVn9Uw1y1iCZscNmQSIDBGft2RyojCfAXo5XM9PjkFPp98pc88LJq+fNfTXRekz9Ax4tT4c9UZRw+ZNTxj3Odtky2WShMd24hS8sAOWQiyjeTvUr4gJIV83hC7FH8xM6QAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(wege3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(wege3['5 dias']))
        col3.metric(label="10 dias", value=(wege3['10 dias']))
        col4.metric(label="20 dias", value=(wege3['20 dias']))
        col5.metric(label="30 dias", value=(wege3['30 dias']))
        col6.metric(label="60 dias", value=(wege3['60 dias']))
        col7.metric(label="90 dias", value=(wege3['90 dias']))
        col8.metric(label="% Probabilidade", value=(wege3['% Probabilidade']))
        
        base=yf.download('WEGE3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'PRIO3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIADUATAMBEQACEQEDEQH/xAAaAAEBAQEBAQEAAAAAAAAAAAABAgQAAwYF/8QAKRAAAgICAQAIBwAAAAAAAAAAAAECAwQREgUTFBUhMUFxIlFSYYGh0f/EABoBAQEBAQEBAQAAAAAAAAAAAAABAgQDBgX/xAAkEQEBAAICAQMEAwAAAAAAAAAAAQIDERIxE0FhBBSh0SFxkf/aAAwDAQACEQMRAD8A+UZ+q+USFlDQaSFcRUtFaBFcGktFUEVsK4gwqWFlDDQYUEWBorSQriNJ0VWsOJwVqj0ZkzrhYlBRmk03NIx3jxv1OuZXH3nwO7MvrlV1a5OLkviWmvf8jvjxyv3Wrr25L6JzNNqEZa9IzTY9TE+71e9/Dwlg5Cqqs4bVr1BJ7bfsXtHrN+Haznx5e/c2Z5NVqX09YtmfUxef3ur5/wAYLqp02Srsi4zj5pm5eXVjlMp2x8PMrbiK1sriSGn6uRlYvYcWE643yjFJx5uPHw+x5TG9q48NW31c7LxyvE6ShZlwdqhTVXW4xW2/l/BlhxGdv01mu9f5tv7TjZuFC23hX2WyW0rVuafiLjl/bWzTusnN7Se3h6SzMfFhhRV0buqk+Th4+Gmt/snW3lmac9lzvHHP7Zp0Yk87tXeFai7Oemny896LLZOOHtjntmr0+l8cfDJ0tkwy8yVlSfBJRTfrr1NYTiOj6XVdWvrl5YmjbpAVraDjDQEhpwUBUtBZQw0GAEag0VWsOUNADQEhpwUMKloLKGGgAEa5ayuQBoMAAkVpxVDIqQsoYaAH/9k=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(prio3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(prio3['5 dias']))
        col3.metric(label="10 dias", value=(prio3['10 dias']))
        col4.metric(label="20 dias", value=(prio3['20 dias']))
        col5.metric(label="30 dias", value=(prio3['30 dias']))
        col6.metric(label="60 dias", value=(prio3['60 dias']))
        col7.metric(label="90 dias", value=(prio3['90 dias']))
        col8.metric(label="% Probabilidade", value=(prio3['% Probabilidade']))
        
        base=yf.download('PRIO3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'ELET6':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAzCAMAAAAKPR4NAAAAxlBMVEX///9Gs0FEebbZ5DUwb7H3+fzi6fLq7/YfZ64WZKzz9vr7/P05c7Ozxd7c5O/J1eefttVEdbxQgLq6yuDAz+P+/vbz97nt8p/p8Ize6FHh5zRGtjWpvtp3msaGpcwJYKvT3esAWKf6+9z3+sru86b4+9Tm7nj7/Ofi6mTw9K/s8pbX4hjb5kPk7G2t0yKZ0p5ywD8qrCmw267H3TjN6MyTyzuW0JOgzzvq9um8z7/e8N4zbblDmIJOh71DnHZakMFEiZ5Fg6kfILffAAACrUlEQVRIie3UbXeTMBQA4BBC3ggJA/ZaAnSb09lOne86u87//6e8Sehx81TnKfEcP+x+KYTw9N7kEoSe4l/FfkTr9CwatX92EA0D6/wyFvbs4PDoMBYG1sVFJOs5WC+WkbbzDKzjNNIOXIK1TK/iYC+vwEoXp1EwWLAUYhkFuzp2VrqIsqEXPrE0ffU6AnYUrJM312+nY+cLj71Lkuv3k7HTRUgsSZLZ9NZ1a3byIXHYx8nY5SI9+ZT4uJ6MoWXIy2GfJ2NfZskG+7qbICnLc5RT0+Gbb7OJmdGmtCtMiFIY791utN0slJu2s6sK+9gLuc12/ghkU3brEcN7d4njdu8zVpd2vRo1pW5nuy6/j3y4p+Gb7xO/ply3oCmlCK+KaVQINhRtYVgM6im2BhsDyS7788zm8R3lXLiYo6K/j8ktM8tHMWKpdoEK/hPL1JYsyF9g3XgRMKk1JMV4jXLoWjiK4IcOOvNYpjXcjsPM1Mb/PTyWW7HSlVwiSYiYG9Ov+rmWVc97Dpmqqu97YpAfHoY5UYJQxDA8nutgqHXRtq0MmBGFA5nk5TBkhnSaIqsoyjvBAKM5rQgauNU0c6sqsUWdYvAZjwkpXFUVDHisI65S0UgoEwHNNqkzUYc1azgdBPVvwlHcVchWv1szq9wJwdsNBm9lonUvwlZ6TIthEK4oXYme4woVAttSb8WwaSDoA6x8iJmAVStoTpcWnFSYm1+wWshQJgq7OWJhgtyUCWMey/xdN9aoRoRYRl0g2tcwFWrKKEztoAECZt2ClnDpVQsb4DNTNmDSddKmBTkZvwBke4Y6QRTHcA3DhZk7jMGAcrUqTuCYbJDxjVAKVSm+QmWvMCfjgUfHcCW426YeXAsOtZGZb1HY+Lrxkym0KTzLdOhVmMnccQyjOfqf4weVRTQWIZ2D6gAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(elet6['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(elet6['5 dias']))
        col3.metric(label="10 dias", value=(elet6['10 dias']))
        col4.metric(label="20 dias", value=(elet6['20 dias']))
        col5.metric(label="30 dias", value=(elet6['30 dias']))
        col6.metric(label="60 dias", value=(elet6['60 dias']))
        col7.metric(label="90 dias", value=(elet6['90 dias']))
        col8.metric(label="% Probabilidade", value=(elet6['% Probabilidade']))
        
        base=yf.download('ELET6.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'ITSA4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAATCAMAAAANkRs7AAAAclBMVEX///8AOogAQosARY1+kbYAR44AQItqg64AMIQANoa+x9nFzd0APImir8kALoNDaJ4AJoCImrx3jbSvutDe4uv3+fsxW5hifKoAIX7w8vbq7fPV2+Y/ZJwAM4Vwh7BNbqKUpMJYdaYAG30fUpMACHkAE3uF3wgWAAAB/0lEQVQ4ja2UC5OjIAyAQSWK+Cgi9Y203v7/v3jhsd52eufNzqwzVZrHRxISCPnG0zP7HfPLZxlv8qdYYpTzT7F0+X8bY7Is63KxdJ0xHS7x3dVepby7HlCaGYvLEpc5LtR9hFbpTAdE3520pQA6EFKPQykkr1ohbLN6TZUGC8uh6UN0LZsIyZuckPkxjlPQZ+Ny0g5GMQSJBkTQJHycvKQ0ZDZvDKJtbVBbFCGnW4BpDsMJu6dUEDLM3t/DyN29VkjXNxiqbcVDnDGymrNmeoXN5AvM6XoY0q3/C0xRdnjnOtSMGQD5CiNfYT4Lu3AwHv0K01uacnsmJhICrLqG6V8TVrOY3mGkT9C7qqNor4kEqi5h9Y6/ClwEU/EKw/MrEsb3UNAPTeYmPS5h4GTUx/8Ow8bgDDxNukoMySYuYOKmlCrX1MWv/8DUWVJVsM11TiHRMIPkcQHb1xafHVLsEt2cMIvNPsSOqMAdbbo7O6zu/E/YPAYBxr+4bIs4OQeW/RGnhzvYIaIjZMGA0c8ZLqskNHMWHXAkUCAphP/2A/cfGn90emsEWZ7RkzPuPj3O5mclDAXmYlC3PRYcxxJ32jd+1KVan27XoXkax8TLrU9i788Iwf2yeGu4MNyt4a6F2uDl4ay8MsdAFtkytlufrJ17eYfqgXHlqHWeZe4g3W/6PSC8aFTF3wAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(itsa4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(itsa4['5 dias']))
        col3.metric(label="10 dias", value=(itsa4['10 dias']))
        col4.metric(label="20 dias", value=(itsa4['20 dias']))
        col5.metric(label="30 dias", value=(itsa4['30 dias']))
        col6.metric(label="60 dias", value=(itsa4['60 dias']))
        col7.metric(label="90 dias", value=(itsa4['90 dias']))
        col8.metric(label="% Probabilidade", value=(itsa4['% Probabilidade']))
        
        base=yf.download('ITSA4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'RENT3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAASCAMAAADGzcieAAAAh1BMVEX///8AVgDw9/MAUgB93yAAVACKr5akv60AaCr8/v31+viOsJmfvalIg1ssdESauqU6fVFilHMAQgAAXhoAWQvS4diyyrpXjmmBqI5Og11tm3wAYiAAajDH2c3e6eKb5lx03QAVcDm70cMhcD33/e/A6abd9sqY5lXL8q6P40F3oIQASADW9ML2a2gIAAAByUlEQVQ4jbVTf5ObIBBlISSCBvFA5QS9i96ljdfv//m6oMll0qaTP9I3zuy6+3izP4CQ/4H+aUo0z4x8mO1eCmJf6J3sACYLj4ttYUfgcC9b25BNt0Eh/vDEt9gt+VrMszJ5O92soVapajh7bR3rr5Ry9X5OYnstmv1rhCNkfFW6adajNXT1opHzItmSWaWAY7rkyStwFjDtrff7JOa5LHwIkzcVyZnVmgebjn58XoaZQ4oM1vdCjNZQHCd6PQtE21yQQa1iGVBBqWhMoJGM1XmDzR/f3n+QGzG3TAXNFlL/Axaml4lcxOKfMQP+5uczP983m7dbsRZS2w24DtYL2EAXDc2uxGRgIyHdQu75HbEZxjQ5KGdolm310KYSzbeY0Ik9L23s/lJZSoxc47LpAeqRT+gJ5WQwsYDuSqyyLpFBIUVOOLMjim1Op9Myt9zqqqpaWUHInYGZkAq8cx7LasDOpbaXNmVhfYdkR1qb5bmJC/jYrJDLGjljDJ+KA8bS7MWWcwaxhB3mQsE0cV8lgS85M4jkAxEd2mrGaOozYr3ENCLtrT7f7rpeczFEJRFUEEnxS4hF0HpI0aiW8Pjb/DeOvxBP0noafgMLCCCGppwemQAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(rent3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(rent3['5 dias']))
        col3.metric(label="10 dias", value=(rent3['10 dias']))
        col4.metric(label="20 dias", value=(rent3['20 dias']))
        col5.metric(label="30 dias", value=(rent3['30 dias']))
        col6.metric(label="60 dias", value=(rent3['60 dias']))
        col7.metric(label="90 dias", value=(rent3['90 dias']))
        col8.metric(label="% Probabilidade", value=(rent3['% Probabilidade']))
        
        base=yf.download('RENT3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'EQTL3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAEQARAMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAAAwcBAgYEBf/EAC4QAAEEAQMEAQEHBQAAAAAAAAIAAQMRBAUSIQYTMUFRBxQiMmGRscEVcYGhsv/EABkBAQADAQEAAAAAAAAAAAAAAAABAgMFBP/EAB8RAQACAQQDAQAAAAAAAAAAAAABAgMEERMhFDFREv/aAAwDAQACEQMRAD8A+DaWtLS133Ob2lrS0tBvaWtLS0G9pa0tLQb2i0tEEdpan0rDPU9TxcGMxA8iVo2IvA37XYH9PWaUXj1cSxmGd5ZHx3YheItpMw7uefzbws75aUna0rxSbenEWlru3+m5sVPqjOJTAAOOO/IkzPuf73Fc8KM/p3KGJNI+oF3hGYwjbFd2IYyrzf4n4dm/dV8jF9TxW+OItLVhal0PhZOZp8GmyTYovg9/IMsYyYq98vwbu/4PXKiH6a0Rd3VnGNzjaMmxXdyY/Ftu4e1EanHt3JxWcFablYOb0ND9kwwPJgxmx4cksmeOAiOXtkI+N3Pv4/yvH1F0vj6D0tl9xo58yHUBjHJYXF3BwEqq+PKRqKTMRBOO0OK3LKjtFuo+h05qcGna1g5ORELRRTCUkjC5Ew3y7c/s1qwpertAbKcf6vkSd+LIF5qm7cW4meNtvyzcWzeuVUm5NyxyYK5J3let5quk+punTyxx2zQMxkhMXigKXusw8s2xn5+WfleQ9c0MtNyYsUiEsiHLZoWwZHKWQifaV7fgS/tz4rip8PLlw8mPIgdmkjextvyr+V7Itdzoo4YxMO3C5OAuPjcxM/PnwT+1l4sR6X5ZWBh6roz5WmZZyyju0Z8WSJ8GR9j/AHX7ls1OPq2vy3PKj6q6i0mbp3Nx9NmkbIH7NHHIMBx7qondipqsb81dP5XBRa5mxtGO8CGONohEgZ2YW21/yz/r8qE9TyjxDxSIXhPbubY12IiLPfnwDN+vypjT9xKJydbLF0jqnRB0XAgydSKLOjwpQKYo5C7cruO13puX4en59/Kg606p0bUNHy4NPyWyJTywMY5IjogYGZ3t2bm792q2tLVo01It+kck7bJjNiK2Bhb4F3r/AGsKLci9DNFuTcotybkEu5Nyi3JuQS7k3KLcm5BLuTcotybkEu50UVogivlZtEUoYtZtEQYtLWUQEtEQLREQf//Z')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(eqtl3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(eqtl3['5 dias']))
        col3.metric(label="10 dias", value=(eqtl3['10 dias']))
        col4.metric(label="20 dias", value=(eqtl3['20 dias']))
        col5.metric(label="30 dias", value=(eqtl3['30 dias']))
        col6.metric(label="60 dias", value=(eqtl3['60 dias']))
        col7.metric(label="90 dias", value=(eqtl3['90 dias']))
        col8.metric(label="% Probabilidade", value=(eqtl3['% Probabilidade']))
        
        base=yf.download('EQTL3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
        
    elif tabs == 'RADL3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAArCAMAAADluJ77AAAAbFBMVEXw8PAAeEkAcj739PYAdkUMgVc/j23z8vMAdELD1c5hnoPj6egAcDq90cns7Oy2t7K1zsZ9rZnm5uakpp/LzMnQ3trY4+Ckw7fFxsPe3t2/wLytr6nX19WVuqs1jGhLlXeItKJupY0mh2GYmpINlEXgAAACL0lEQVRIie2W25KjIBCGEdA2YkDBeEhIiPr+7zgNrjHOnnDudmv+sgQa/KTtBiHkW/+54KXfW2IlTqsuwBYT1s9VVZ1PF8HYERbLSroqvQdLvVn44y4O4FjKk1W8dBItRZ5sJppW8bR3WJJQB3uYf8MzmhZgPPjkGWUHC4y+TGiLpXkYn05n1EgR+2ALrPKWbqT+VbyNDGuAZcznQaDkwhc8lSE12GVCGx0jp/YD5qtQ4dToZYGJpRtE4r9p5NT+AiMsGLujMGCOb26uMAI4II/0c4UxJkIAMvYJxgoc4A7BoJ6SkBFnjAPdw3If4yMwwZfcTU8MWlfyZINlh2cm1oQv3YWxe1KsXxxanxv1l2aGEeBPYHLrH/Pg/BEYKXARlnkglg/0de32mYEpHMV6wYDIthpTv3xwqboKdzKUfNIji/M9aYGJe4ip33ncWNdF6ll5FofawUJTFGXwlfMc5at5KmK3708wXAfVRHdb3BS7Z3hYzukuJ4F0uJXnPIjSWsb/VqBzzlX78cDabszSJJncvT32R2HAfno3xgKkEPIXXX+U1OGGD8mdQ0C0liB9hkVmGT4zm6vUupGDNHOP9wHwpvHSvRr0rAB6cwCmjLmqGxbEV02DTWPUfL15WA/EmCHSWQ+7KaVMfzPWKOvLXhk0IH6QzWwtjrCRNCttf7XWKntVQ6Ot0mruG4XtxmqtmmHQxMbC4O2cAr5Brkq/zi3L4eX4CWbDf/3Rb/2r+gASzyGasEu3bwAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(radl3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(radl3['5 dias']))
        col3.metric(label="10 dias", value=(radl3['10 dias']))
        col4.metric(label="20 dias", value=(radl3['20 dias']))
        col5.metric(label="30 dias", value=(radl3['30 dias']))
        col6.metric(label="60 dias", value=(radl3['60 dias']))
        col7.metric(label="90 dias", value=(radl3['90 dias']))
        col8.metric(label="% Probabilidade", value=(radl3['% Probabilidade']))
        
        base=yf.download('RADL3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'RDOR3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAA5CAMAAACrpj1rAAAAkFBMVEUAPon////+/v4AKoEAOYdYbKAAPYno6/EAO4gALYIANYUAN4YAL4MzU5MAM4QAMYTN1uWAlrv1+PubrsrV3urCx9gTQ4zu8fYAJn8qT5EAG3yUpMN4jrdEaKGxvtQADnkyWZgAIX6nt9Blga9heamKncBSc6dBYZshSo9xhbCeqMQAAHZAW5ff5e8AB3i3x9tHMzdvAAADtUlEQVRYhe2XiXKjOBCG1UYREpfEaWOOYDCHiRm//9ttCzuJdzZ4smNqt2pr/5JpgcRHt9SSgcCKIrDRup5svqN/EvYlZvGOB89ZGbaiiLmiiLGiyL0Yw8Kuhjwj9pfKs2Jrstg77/kwHwKolBbVFY9/PI993nd/7y8dcY7h6DeUMNmm/CmvCaPhiXh2mvOUBEf66/4P3GNWefZmZttY6ubZcphanHLsxjhqPuhLuo7j1TTIoh3vM0ITm380LPnFmOu6KbUHNO5cJ5LoesqI1c5u5El5Tj3XHRw6t3sfE/9zWCzRS3U7lNq4gd4e8vlSJIjt2zjyfqKSqtvipXg/bx8n64v4brBNYbGgrae9Ze2DzGFZMGwaYdmM0ONZEv8la52qDjwvh3QzOp5SxlegG6w/vJltbXbNEWGSVuBusmNTcIzk5OdpFRm8L9UOG86bbP9aKvHu18/uIUzFSvEaoijaIYz3GK0ZTaEeGtuyDVXY1YAEjrBgusRmv5gjCKuzGop6etsf0LOd6DGa7nVvYEZQymTtS1KIUu2lhsXZCK1cnM0ECvG6yesgG0caqHGcIg7xOOZWeuy6xD8avEtkBn4eAwV/9zrFxl2m/TnSRPVc1l2LUUZurKIodhM8RrV4ybvGb/qi093qaVLHnWqoDDNvKUxCBCaj5B7umIILPDqcaSMxTzGn6JBQ/XTpSGETLEQ+YD0Q++1diUsp19ohaRdfLsPTNOoI4RBeZFmGMNsx9MBgeI6wHaFTyhJS/7gjuBSohczQ8rpSqTKxTnFZplx0l0k1DrKGMj5iocTy41r48TjEcVXHqJAuBUALAHMKhv2Ea7g9ZLiQ0XqEuwB+oGtOCdtDCWYK0E+6dbKXYJYPkFeCnmETwnTYwuVNQUARtnmH1WAibEJYYYkcoLSWouSD3lyiJAPVY2+A8BACpJSmV5hkxifs5dAC1MbyNHm7YkTnIsh2WwixvNUAQ5L01zDZQDHMH/U1TGxqf4hlVmvGCu/DnjscGNwjY4DL9e3GD2aDZzigYYVdcMSCwFyE0W4KguiUT8qxm2iqwm2wDROlFTU3c5oCs5YVtupFG6lFGOHGbmdYliEwxwyDSlygThLOKrLZdA52kYwbxrx2DedvpTYbbmFe3yPbxdn7Fow0TZPPs1kfm6Z67q8ct2tvuKYGjsCTrwWoz6RdQZ/LaQWxVKdGdLLXgBFmGBaWVVj/EVFq03fZNhb7auhviLysqHU/xODuo+++4Vsfsl98Iv4P+xdhfwDbjVSkrUQZpQAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(rdor3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(rdor3['5 dias']))
        col3.metric(label="10 dias", value=(rdor3['10 dias']))
        col4.metric(label="20 dias", value=(rdor3['20 dias']))
        col5.metric(label="30 dias", value=(rdor3['30 dias']))
        col6.metric(label="60 dias", value=(rdor3['60 dias']))
        col7.metric(label="90 dias", value=(rdor3['90 dias']))
        col8.metric(label="% Probabilidade", value=(rdor3['% Probabilidade']))
        
        base=yf.download('RDOR3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)    
    
    elif tabs == 'BPAC11':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAeCAMAAACxDwjlAAAAb1BMVEX///8AAB/7+/sAAADx8fKoqa9TVmVxc33Z2tx9f4gAAA3R0dT19fbHyMuNj5fk5OYAABjq6uuam6K4ub6wsLSTlJuDhY5gYm5naXUAACQAABMAAChJTV3AwMQTGzYAAAYADy9BRVY6PlAjKT8tMkYGK5FEAAACXElEQVRIiaWV7ZajIAyGEaGAfFVAtFa7nZm9/2vciHTaWm3PtvnhIREeEgyvCF1NjU00JjZeoU/NiobPI94w/hkruluPsg9QpCX3AdXWb7O6xxizb8LatWCH32IJshbFb50bp+txr9+A5QzGuGwI//8skptiqOQ8UH4j1ac2l0FzE+yKDOPl8HLp+HBL5oaI2dsddGgoNAQvBi6hZOmSu2rmAcbuYadDWe0rj/jhVJURdfvqT1+lM2CMdQTZjrEAe4FTu46JtJJ7ZOA1yTBzgZ07gv3xAJl96bGW+2+L5bmHFISdrkSa5CRufzOb1vMwuRBcwNKZfRc1L3bTsmL6DO0U7HIZMmhLdTppQ64w5X3NlmUWPD3tDGsSjBU6wwQygesheLmAkVZyd1zAUhJouMBc4VLwCktr6bjIzKePtCzTHGBEjj2y+xNM5f2P5uF8hLUnlaZPhyUDSascR/OVDjLIG5jOt6beFz9DsQfi16EqHTJ9VVZ/J1gnYgRJGtsYBbRYJ5jFO9Eg3TZTAF53OvcZFJBpcTd06QoFI2BnImHKVDtsOitI1hGMLw+Ff/1sbksHMdbnSm0o1JZtaI0oy76fPumqQm2ZDmvRMVIaLteJ5ousLxWpcYvm5GOMx7sZaD6LGmWNUasJJDMP+0hxHQcKfyuqYjCQYaTcUqfxNgyFeO83t3++ZsqMBoI4iDK8wJq7ZzBUsxtFDO2d6LoZppCdYYbU8SkMfulRUM25pkIsjtDUqgENddwADPTCENXgl2pca+/1SteNniOLsNXcgkbUeBwn/yML4UU2/wBZWh5qch8KjwAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(bpac11['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(bpac11['5 dias']))
        col3.metric(label="10 dias", value=(bpac11['10 dias']))
        col4.metric(label="20 dias", value=(bpac11['20 dias']))
        col5.metric(label="30 dias", value=(bpac11['30 dias']))
        col6.metric(label="60 dias", value=(bpac11['60 dias']))
        col7.metric(label="90 dias", value=(bpac11['90 dias']))
        col8.metric(label="% Probabilidade", value=(bpac11['% Probabilidade']))
        
        base=yf.download('BPAC11.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)    
        
    elif tabs == 'BBSE3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAxCAMAAABH9b8GAAAAnFBMVEX/7gD/7wH/8gDAw1L/9AD/9gD/7xn/7yj/8lHa1jv/+AD/7yL/8Ub/8lQ0aJ347BLl3jH16RvS0EP/8luYqG+zu1qhr2pDcJiMoHehrGzv5h4AQLSOoXSxuWAATKxvjIhoh4vq4ijOy0qGmnpdfo50joRVepMAUql5kYK7v1l+ln3Ex0wcYZ8VV6ertGb//wBNdpcAWaQZX6NcgoxlzTyZAAACAElEQVRIie2Xa5eiIBiA42aLTYiE19HKLENTd2b6//9tobls28aemjz7yecclTfkCfDFy2RyDnBm05njADC5AeDoc/Xuab5YLOY/NLe0sutOu9l0Op3pLjjOQ7IP5W0DGRkZGfmbs9sHMGAAILiH6zJTQ7gkOMAQ4+stdcXlX1llJIxiFko3kEkKCYQYYKwPRB/1RggUUlJiQvOjqbfLPPac5eEyd6NktYarYlOmebBFm610s1XurXZAVvU+UCXJEFWlqEvfLoM8rppKYrfasgNqk/w5UF0atunSY0WXybgP2TpWh5aySh1/5nFb/GOYyUsZZRV1X/pstZNR3rCmI6TzXj2WtqpPwvAoXlWzRk2XlqzPWArtPdMT5u3fhBsdI9WhfVyzhslqGy4Jy9r6WB2SVrEdiqLw2Bz2WfyWFDYZpBFvWUkg4JRDTjj308JHHkAF5hRgIUhKKSz8lEKf0sIvuPCtMh8Twl2or5LOAJMfpmAu2qn8EcPP4D36Y5xfZUDRt6BXn5oAfkFc/A4xYNf0wMb1J/DvpMZ94wt/U6QcUVQLT1JhX2LW1PhcNIdMlXES50rsArlTuVLe92W0LwIU0UD4eqt5zoN7e3Zm0zcOCDwzIWYiT9G9sss5tNYM2eQ/yYZ43RtlDzAbUjYdZXfzNKhsyMX52HfdBfMBs/YX/5YmGqtff10AAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(bbse3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(bbse3['5 dias']))
        col3.metric(label="10 dias", value=(bbse3['10 dias']))
        col4.metric(label="20 dias", value=(bbse3['20 dias']))
        col5.metric(label="30 dias", value=(bbse3['30 dias']))
        col6.metric(label="60 dias", value=(bbse3['60 dias']))
        col7.metric(label="90 dias", value=(bbse3['90 dias']))
        col8.metric(label="% Probabilidade", value=(bbse3['% Probabilidade']))
        
        base=yf.download('BBSE3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'RAIL3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAEQARAMBIgACEQEDEQH/xAAbAAEBAQACAwAAAAAAAAAAAAAABgcEBQECA//EACsQAAEDAwMCBQQDAAAAAAAAAAEAAgMEERIFBiETMQcUQVFxIiMywVJVYf/EABkBAQEBAQEBAAAAAAAAAAAAAAACAwEGBf/EACARAAICAQQDAQAAAAAAAAAAAAABAhEDEhMxUSFBoRT/2gAMAwEAAhEDEQA/AM7REXoT4gREQBERAEREAREQBEVW/wAPtdZQyVrxStpo6PzhkMpsWWLsRxy6wPHb/VEpxjyyowlLhEoi7bW9v12iQ6fLW9HGvh60PTeSceO/HB+oLsX7F1lm5I9AcaXz0kHXH3Thhz6278H0XNyFXZ3bldUTCKwd4bbj8oZ4o6SaRrg19NFUAyxk/wAhaw7379lwdwbN1TQdPh1CqfST0kr8BLSzdQNdzweB7HtccLizY26TDxTStonUVRp2wdw11EysFKyngkAMTqh+Od+3ABtf3dYKeraSooKuWkrYXw1ELsZI3jlpVRnGTpM44SSto+CIiskHsVofiy9507asRcemKDPH0yxYL/KzxeznudbJznW4FzeyzlDVKMui4zqLXZqW6NCrd0aHtGr0psclJDRCOpmdK1rYOGXLrkcDF17ey7+q58a6O39T+3rDxLIIXQiR4icbujDjiT7kdk6smefUfla2WRusPzOqvv6bb6u66NH2bLI2k8R5WvIk8tK/IHnL75v83XHpi1vgtKXtDmt1MfSfUZN4Wfh7gHAOcMvyse/ymbscMnY98b8K3g83ftfCVm8cdmk69oOoa+6h3LodVV6nS1Qa6rgbUND6Y3u5jRcANA4t6Ec3vdTniTq9PrW7amppGtETGMiDg4HMtHJuOPW3c9gpgcBwHAd+Q9/leF3Hh0u2+CZ5dSpIIiLcyCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiA//2Q==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(rail3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(rail3['5 dias']))
        col3.metric(label="10 dias", value=(rail3['10 dias']))
        col4.metric(label="20 dias", value=(rail3['20 dias']))
        col5.metric(label="30 dias", value=(rail3['30 dias']))
        col6.metric(label="60 dias", value=(rail3['60 dias']))
        col7.metric(label="90 dias", value=(rail3['90 dias']))
        col8.metric(label="% Probabilidade", value=(rail3['% Probabilidade']))
        
        base=yf.download('RAIL3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)        
        
    elif tabs == 'CSAN3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAABDCAMAAAABHxPMAAAAyVBMVEX///9/zEUFeLUAnNkAdLMAdrQAcrIAb7EAbbAAa68AaK14ps33+vwAmeB9y0F6yjx2yTPg6fLm7vWZu9cAmt2/0+VBiL3w9fmd13fX7snk89vv+OoAk9al2oMoo9yCzjunw9xVk8KQtNTP3uxonMezy+EAYqsxgrr4/Paz35iL0FqGz1GT02e946ZwxyRnxAdnteLC3vGjz+yIw+4io8VivIXL6blSq91Ps6NtwnF0x2N1veWNxedmvn46qrp6yVNJsKlXt5aU0JxR4DC2AAAEGElEQVRYhe2W6ZKbRhCAh9FcgIQ4BEhrraVByOzlTbzxkU1iO8n7P1S6e4RuuyzYP65KV6lgrm/6Roz9qNzMbqd3nnf/cP129sOHzsvs4TEeR5HneVE0jn+56oG6uouR00rk9WBdH6A8b3zbGXVzP/YOJe5s5atxdMTqbuXNCauDlb+W7nl3wrrcynfz+RM+b+MTVnR/sWKDweR1wq5OWR2sHKDMf5ueGnm5lcmcaO8XxyaO4/jiWD4Ra/ThAAag6e3H2cVJ9ifBJgdKxdcdc/XTiZXx9FU3FGOvSbHfd7D4Y1fUJph7Lov7tDAHe45eQK8W9scGFk37sJzPtrC4s+9JPu3Dxte9WC7PWp9174VOniaYGptojvuxWDrf5Vn00BPmIuAqoK/LGPuL7Iy69a9jITtHn6MXgWGrHUy+LF4GlpKdX18kAKmleP696J8aw0oLTl3oa9Q7aSufc9m0XuvrNMmBNm97Wk87Vz7SXLUvvPHbfrSlAZpzG9B69iBWmdbSyfPi8n8EZ2kYhdE/i8VdT9qS/Iamjt4/P3o9m9pKqh3u8+P1nuOGHXBhIAgHrhsNvnz4d3Z1A8XxLjRhF+US6yvIOSl5M59MRqPRfC6V8fm6CwxwodKCclgKCT+ljc27oUjysFFGoxjN62XZA0VSJvl6vc5XvUH/y08nw6NqOxqW5XcWYSLdrSdhIwTfJfbaQj0WWXumDLlS7XJSFbDYZG6psUXI0lpANlduJvQVFIuUpkhpO9dYOFCDrgJXhpqHMEXJhrAX16RuSJdAinplqNx0gxNW41YF/UFxPOvDEg2lj/eXwXaMA3gorH1BZwNon9AFEMb1EvQCllJhVWsRJNBgDKxoW9V4wgfTMtALlq02sJlVWhdVVsOcyQkGIKGbBiakZWmAe8k1Fh81qpCgUy32MrhMcFXRMrnakitC5SbhMFc1OHepQUdWgb+KXZRK6NV+4oZwKVwPG3izOoxdmisuwo1mdHqIXwxmJdd7/SnXXNjNe0bXo+rcFG07LKtC+D64poW500MMEuM7TVCWANiEna1A9Rr42LulFnRoSZ0XPd7CTHkAM9+HsaQI2tjiF0v4qinkFiaGOxiYqfY6em4OzBQuFZMQY+ynDNRSYUn3nINh5JvN6bVzpO/cPQTHGHil8KUN+HadGIwZoxCfg2EaKot2l/WbnIIu1WpznE42ReKOE4xTYht+FgZpiEldhxb+30GOD6E2oLBqq6XTcalxWChSE8wUNs+U/AaM1fSnAutLgFdYotHbEmMWoDO3QywgLBehFX7qz8NY5kPlQXUGZC1LC5++kJqvNkMFY6pzxgrUXwRrozTC3ihlHAw2CZeIy7oo6mybIavKNkWY74a1te1wXcNSwrJlhhNVlrlONYSX7D+PF0wCYcz80gAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(csan3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(csan3['5 dias']))
        col3.metric(label="10 dias", value=(csan3['10 dias']))
        col4.metric(label="20 dias", value=(csan3['20 dias']))
        col5.metric(label="30 dias", value=(csan3['30 dias']))
        col6.metric(label="60 dias", value=(csan3['60 dias']))
        col7.metric(label="90 dias", value=(csan3['90 dias']))
        col8.metric(label="% Probabilidade", value=(csan3['% Probabilidade']))
        
        base=yf.download('CSAN3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'LREN3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAYCAMAAABnVuv4AAAAY1BMVEXjBhPiAAD////hAADjAA774+TkFR/99vb3x8jujpDyqarwnJ3vkpT87OzjAAbuh4nrcnX98fH30NHnS07oWFvztrbtf4HqZ2r52tvlLjP1wcL41dXpYmT3zMzkJyzmOT3mQ0ZdLpsOAAAB2ElEQVQ4jdWUzaKcIAyFOQkMin+oI151HO/7P2UTnWmndlm7aBaCnPCREMDQhWYow+0agxcY22uMFQZzjf1DmAVQXwOzPJWhnNjqD9SkrbW1pj4GPzuH8PY7wSzmvbyzuBiMTZ6PMPVd2nLCfZKIEZ91v2lnnNCrsEH1CHuG8RdR5cmTY3Ff3Nj4BQh+jPGJ0Mogux6513CWOwoSYcLgx1RVB+0XDCVR5HEGtyUMuozxpAeHiiUbmTqzLNejoY5FFdghDI7BlON3GLcUAiaX2LV8wKY3zCAMMkFh+UAF/4SZHYYzzEK26yELUyu3wqL7ihKEphlTqhFiQXeFlSmXJRSmAjC0MbXnNO1NMMx+r8FNYQUliTD41DQCS7wQFJZzRmZVWGpyhTUS6rkATBQ47Sx/7FnnFPZKU4LwblEYuKrWzzQD/VFNDDSx22GDwlY2shUKU1FhE9G3wmpJolfYPkv2zA98glnji/B6SLT4K5DTfia0aKGRBeIBM3iQRHYIgwT4EPbpnGE7UH6TfxQFDM8lpzXLVinMQwa52BCjquU3ogqjVFf85Bicr5OEsriuPG7H/tVNwX5fX4P2s7NfpLffGSaDzPwXT8j/8p5dAJv5KhOYd1cZ/QDtth4b5P6eIgAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(lren3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(lren3['5 dias']))
        col3.metric(label="10 dias", value=(lren3['10 dias']))
        col4.metric(label="20 dias", value=(lren3['20 dias']))
        col5.metric(label="30 dias", value=(lren3['30 dias']))
        col6.metric(label="60 dias", value=(lren3['60 dias']))
        col7.metric(label="90 dias", value=(lren3['90 dias']))
        col8.metric(label="% Probabilidade", value=(lren3['% Probabilidade']))
        
        base=yf.download('LREN3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)                
        
    elif tabs == 'HYPE3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIABYATAMBEQACEQEDEQH/xAAaAAACAwEBAAAAAAAAAAAAAAADBAAGBwUC/8QALxAAAQMDAgQEBAcAAAAAAAAAAQIDBAAFERIhBhMxURRBYYEiMpGSFSNScXLB8P/EABoBAAIDAQEAAAAAAAAAAAAAAAABAgQFAwb/xAAtEQACAgEDAwEGBwEAAAAAAAABAgARAxIhMQRBURNSYXGRweEFI0KBsdHxFP/aAAwDAQACEQMRAD8A3GiE51/uAtlqfkhSQ4E4bCvNR6f70rtgxerkCyp13U/82Bsnft8ZTbHx+lN2Ztt2lMKW8oIScBKkqPTONu3rV7qOjxgE4+fEx/w/8S6pyPWW1PeuPtLmxdW3rncICWlhcFDa1qOMK1hRGPtrPOMhFbz9J6AZAWK+IO0X2Fc7W3PS6hlJYD7jbjidTSDkgq32Gx39KeTCyPp/aJcqsuqHTdraqUmKm4RDJUAUsh9Os5GdhnNR9N61Uaj9RLq957Fxgmb4ITI5lgZ8PzU8zH8c5paG06q2j1rem94A36zpStSrrBCUY1kyUYTnpnfbODUvRyeyflI+rj9oRyNJYlspfivNvMq+VxtQUk/sRUGUqaIkwQwsQtKOSiEyzi/iG7cM3WWyqE08X1qchzn9S9CFdUpB2BScj6ZBrV6bCmdBvVcgTI6j8jIW02TwTvXuHiV3gy2G8qmlyM69LlPtoRLKSQ3uVOqUrvgpOPM49asdS4xVVVR+0rJgOdd7uwR9ZpLvDon8S3qVOZkBlbLAjrakraCyEq1fIoZxt1rNGfTiVV53va/5mucOrIxPulZctlxgwLXbmmgmXeLWLe+yojLRSrJcI8wELWD7d6sjIjMz9lN/H3fOpwKMoCjkivvGHYT0wXq1W+1uuOG7NluZ8ARHCQ0ckk6sgA9B51EOF0Ozfp488xlS2pFHfn5RiLYZrd3UiXHuK0C7GY07HTH5SgV5ClLP5g2OCOwwKi2ZClgjit7v+oxiYPvfN9v9h4NpuVv4Ps8eLB5MlLo8bymmlvIT8WVJ1/CTuO+xqL5EfMzE7duaklxsuJQBv3nZ4JgyYECaiW042XZzrrYcCQpSFEYJCdgT2GK49S6uwrwJ16dSqm/JliqvO8lEIKTFjy2i1KYafaPVDqApJ9jTDFTYMRUMKMkaOxFZSzFZbZaT0Q2gJSPYUEljZgFCihC0o4HwsfxXi+Q34nRy+doGvRnOnPXGd8U9RrTe0WkXqreJvwgmc2YgSwFqU69oGnmKyjcgdSQMZPegknmAAHEG1bJTTLLSJagloDoT+lI+mQdvLNKOE/D3g4lQkufDjALij009d9+ivuohGLew9HaUl94uqKs5JO2w/sE+9EI1RCf/2Q==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(hype3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(hype3['5 dias']))
        col3.metric(label="10 dias", value=(hype3['10 dias']))
        col4.metric(label="20 dias", value=(hype3['20 dias']))
        col5.metric(label="30 dias", value=(hype3['30 dias']))
        col6.metric(label="60 dias", value=(hype3['60 dias']))
        col7.metric(label="90 dias", value=(hype3['90 dias']))
        col8.metric(label="% Probabilidade", value=(hype3['% Probabilidade']))
        
        base=yf.download('HYPE3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi) 
    
    elif tabs == 'VBBR3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAtCAMAAAAz4X3mAAAAhFBMVEUARBX///8ARBQANwDz9vQAPAA9YUMAQAwAOQD4+vkAMwAAPgAAMQAALwAAQhD6/fsAKAAAGwAAKwDt8u7EzcWls6fN1s/k6eXY3tkvWDaTpJYAEwC4w7oAIwCcrqDe5uBTclgVSh+AlINfe2RGZ0oACwBshXAdUCh2jHoAHgCKnY2uvbFOMNS6AAAB9klEQVRIie2U23KjMAyGUWyCMacEc0wgJCELaXj/91v9QNuZzs7G90UXshDmk2zs33E222yz32c7tnWYw92a+Mz9mPd/lhIiYITggUPXYSdEpF3H8RDpSMWY5+IhfsNyjfQvaqc76U+ZL6sjOynL7Kq8a8KR6fKb5zjqxelk772B+UR3N+iJ6CGJmj8JLTaEpzXyb/EuNIhsYL0bFUTljqffb+yynB33SCRf/IIuai5mrGCjW4MzsKufaPHYEHVnbiZrNb+fBIpVlRVM64koOeSro+DATTUBR6cQnT4Vij2lDcykijdqOlZc/cyuTNHjHisbasaapVhgtWdF+8ICQ3Z5u2667NN8DYvRQ7F8bwVrziV/ctjPnSyAqtZhsYTZGLh3HsenFex0BUbPX8A1FVYZ8maWjcQqUxT7uFjBeuxLJPgPypadaQ+MmEYmvo74uQGK9VFjBcPck4pQHgvOQg0YfsJD88FNcOBMGlVWMOx07CmcToF2PsC5I5tq5lRzUkXSBubjFmlvXgvcBEySciNdhB5zXKs4FpbXCbPU/MnndaSrxkEROLLDUqy2gRmWhiJ0ROPLrm0gGaa63MQjkcmgap81xYdcuH3yVjVmPROKBS3AEMwSFrKExdC5xXPKW9TtjZ59y+k/ZNb5EuDvxGabbfbb7C9NPSDBWSYyyAAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(vbbr3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(vbbr3['5 dias']))
        col3.metric(label="10 dias", value=(vbbr3['10 dias']))
        col4.metric(label="20 dias", value=(vbbr3['20 dias']))
        col5.metric(label="30 dias", value=(vbbr3['30 dias']))
        col6.metric(label="60 dias", value=(vbbr3['60 dias']))
        col7.metric(label="90 dias", value=(vbbr3['90 dias']))
        col8.metric(label="% Probabilidade", value=(vbbr3['% Probabilidade']))
        
        base=yf.download('VBBR3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'ASAI3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,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')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(asai3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(asai3['5 dias']))
        col3.metric(label="10 dias", value=(asai3['10 dias']))
        col4.metric(label="20 dias", value=(asai3['20 dias']))
        col5.metric(label="30 dias", value=(asai3['30 dias']))
        col6.metric(label="60 dias", value=(asai3['60 dias']))
        col7.metric(label="90 dias", value=(asai3['90 dias']))
        col8.metric(label="% Probabilidade", value=(asai3['% Probabilidade']))
        
        base=yf.download('ASAI3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)            
    
    elif tabs == 'CMIG4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAUCAMAAAAQlCuDAAAAeFBMVEX///8BXz0AXz0AUSYAWzfk6eYAVS0AUildh3IATB4AWTT+kAfe5OC7ysIATiFtkX7+iAAASBX+hAB4mIf/6t3U3djJ1M7t8O5ljHiIo5VNfGWftKmxwbiou7D/8ur19/YgZUY1cFSTrJ/d6er/uX/+wZD59O//x5ko8vlUAAACTklEQVQ4jYVU6ZqjIBBEUBDGI8bEK4cmuzv7/m841Q1onMx+yx+lpcqqPhAirHNZnsNrFlePzVx2IVyURXjry178gIuRvDJam2rA8XmpVFh2EJnV1cRnLo1uLv403jxBMXhc/sLX2lQmWDJtruKik7ikLUaXJJYVUVjz8cElrqaXccOVkWvSFJIcT8QjfSVLEHVPkqMQUKwgT5OUyHKz4tIp6sI/pSNbTqaP2cpEam+zaTOiSB449YRETxvJRrPhdB3yRWjVZshA27jiqrHrYgGYQlbItxe8bGQZ4+qCcHqaPRk+SRUsz7xlJX492K6+ib7iLFTZSlY74G77QpIt1257gGDmfjqd7iJSICNXHWkjGUymA/VJ4Rf95oygylauEiD16/fxcDgc/4gbUcCNZcEx0UxG2TSox9gYzq+xE6Ol2YSR+OTz+EHrKCZQLCi/Lh0kLpQ+n4m0hQhZQVcjY+1V950MUtx4D2Sf5PlGeVsAMSVM6HJPNm9k+LS32WFnOuFt/mXPGVeU3IrFp2ln80k2DSUBu30BKDWk0xegRqFT364kWGAcyMV7AXpqCTvvW+OCnnb1znPrB4kFEy0e761xBS7N9007KKpcJnrfslRLYAkGlwpnHbN/b9qsZdx5P07s/Cnyxk8TxU1oFz+NrSPfP4wT0t++Dbo0gyirddJ9VmYlfRlFxxUZ3gdd6jjp2xXkLCa5eyFTV/5bSK8QsFYV9fsVZF9maL0cuUcmu96O/n9do8Pp0arHfy5H5nu5ftd7O/Zfv347d+Lf1/YXg2kkAacoaQ0AAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(cmig4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(cmig4['5 dias']))
        col3.metric(label="10 dias", value=(cmig4['10 dias']))
        col4.metric(label="20 dias", value=(cmig4['20 dias']))
        col5.metric(label="30 dias", value=(cmig4['30 dias']))
        col6.metric(label="60 dias", value=(cmig4['60 dias']))
        col7.metric(label="90 dias", value=(cmig4['90 dias']))
        col8.metric(label="% Probabilidade", value=(cmig4['% Probabilidade']))
        
        base=yf.download('CMIG4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'TOTS3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('http://t1.gstatic.com/images?q=tbn:ANd9GcQnJ6ig_GqwP_Om3B1e3UgNTUr-MGzMVFDXWuwKWNqoSiptX8Z_VnZe')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(tots3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(tots3['5 dias']))
        col3.metric(label="10 dias", value=(tots3['10 dias']))
        col4.metric(label="20 dias", value=(tots3['20 dias']))
        col5.metric(label="30 dias", value=(tots3['30 dias']))
        col6.metric(label="60 dias", value=(tots3['60 dias']))
        col7.metric(label="90 dias", value=(tots3['90 dias']))
        col8.metric(label="% Probabilidade", value=(tots3['% Probabilidade']))
        
        base=yf.download('TOTS3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)   
    
    elif tabs == 'KLBN11':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAA1CAMAAADcZP0QAAAAhFBMVEX///8AnlkAnlgAAAAdpmcAl0r8//8AmlEAnVXo9vANDQ3j4+Pr9/IrKyvg4OCDyKWw3MYcHByp2cHg8un4+PhlZWWpqan0+/h9xqHV1dUyMjJcXFx7e3sTExOOjo6vr69ERESS0LLS7OAAlEEuqW5UVVXDxMRvb2+goKDu7u67u7tNTU3QpuNJAAABt0lEQVRIie3V23KCMBAG4IWVgkEQ2ggCotiWivr+79eVU7C0doEbO/a/QTLDN7s7SQT4Pd6MFW3PsJ4NXWPEWP5hy7vTuh7BeoTZ32uPYHAopgUmpzBjzbI6mF5ndF0K002ritbTuHW1mK69zsuEe3NsXQ1m6S/1uzfK8kKF6cr6ulNYPXpvTy12y+Lte7PFLGuqpbXYVIvOkN5gava9k8U+2wqbOPvLVw2mTZ1XuRtqbBbWy0tjbF0KM37QBt2F7czMb7Vh92qL6eZ7XxvS4xWm9Wsbekd3sJ42+L+ji2nXnXJ7VFHH6RJV29pg1mV1Y3Qx0hZNbax7df4l9eqiyjy8/fV/HjdS/ZLXT36iSIKMIsgct7HiuFLidokbxAgS3ICDLYaiwpLcHogJtAPMocLsiD6XIpV21MgALp8U6Un4ssJyRDwQ5qwQc0lFuy4mtLhlY76PH1Bh9DzQi0g3UYYF+Gi7iJutSI9sLBFZje2SLMYAhDjCDlcV5tBYBbdRgW5G879gJ1y52xoLqN8SOwP4QzDq5USYXeCGYML8PHBoqcSygRgUVEuMrjxjXBCG5wBTGvoN7BNNDCHnvM9KVQAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(klbn11['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(klbn11['5 dias']))
        col3.metric(label="10 dias", value=(klbn11['10 dias']))
        col4.metric(label="20 dias", value=(klbn11['20 dias']))
        col5.metric(label="30 dias", value=(klbn11['30 dias']))
        col6.metric(label="60 dias", value=(klbn11['60 dias']))
        col7.metric(label="90 dias", value=(klbn11['90 dias']))
        col8.metric(label="% Probabilidade", value=(klbn11['% Probabilidade']))
        
        base=yf.download('KLBN11.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)   
    
    elif tabs == 'NTCO3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUaoqJnEb_gammVUCvxOBpVIt9Wh6JiFfGSaNjsjJ3RA&s')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(ntco3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(ntco3['5 dias']))
        col3.metric(label="10 dias", value=(ntco3['10 dias']))
        col4.metric(label="20 dias", value=(ntco3['20 dias']))
        col5.metric(label="30 dias", value=(ntco3['30 dias']))
        col6.metric(label="60 dias", value=(ntco3['60 dias']))
        col7.metric(label="90 dias", value=(ntco3['90 dias']))
        col8.metric(label="% Probabilidade", value=(ntco3['% Probabilidade']))
        
        base=yf.download('NTCO3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi) 
    
    elif tabs == 'HAPV3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5GY3oxgCq8cscIT_zFVShXdvxFBZyZpaRqMknc8n_zA&s')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(hapv3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(hapv3['5 dias']))
        col3.metric(label="10 dias", value=(hapv3['10 dias']))
        col4.metric(label="20 dias", value=(hapv3['20 dias']))
        col5.metric(label="30 dias", value=(hapv3['30 dias']))
        col6.metric(label="60 dias", value=(hapv3['60 dias']))
        col7.metric(label="90 dias", value=(hapv3['90 dias']))
        col8.metric(label="% Probabilidade", value=(hapv3['% Probabilidade']))
        
        base=yf.download('HAPV3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)   
    
    elif tabs == 'BRFS3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAEQARAMBEQACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABQYDBAcIAv/EADAQAAEDAwMCBAQGAwAAAAAAAAECAwQABREGEiExQQcTUWEyUoGxFEJxgpGhFRYj/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAMFBgQC/8QAKxEBAAIBAgQEBQUAAAAAAAAAAAECAwQREiExQQUTImGBkdHh8BQVMlFx/9oADAMBAAIRAxEAPwDuNAoFAoFAoFAoFAoFAoFAoFAoFAoFBqzrhEgICpTyW93wp6lX6Dqahz6jHgrxZJ2S4sGTNO1I3aR1FDGDtd2k8K2jH3qrjx7Szbh2n5ffd0/t+b2SUeSzJRvYWFp9u1WmDUYtRXjxW3hyXx2xztaGWpngoFAoFBgmymoUN+U+cNMtqcWfQAZP2o9UpN7RWOsuPv3ld2uapqnMrcHCfkHZP0rMamMl5m2Tq22LTVw4Yx1jlCQjyvNUPKWcDqPeq2+KKxzhDfHw9UjBvT0GWHd6C2jHmp7lPcVLo7fpcsZK7+/vDmzaSuanDtz7f6mtb6olWCTp1mC0w4Lrcmori3ATtQojJTgjnBraMt0Wlp5p4EsuIcAOCUKBwaDSvt3jWS0zLjKOURWFPKQkjcoAdAPfp9aCt6Iu+r75IRcbxBtkOySYqXoqWVqW8d2CnJzj4Sc8DtQXSgi9UxXZum7pFjjLrsVxKE+qtpwKkxTFclZn+3qmTy7ReI32ed2JBWPlIPGDUut8L9XHj+X0aDw7xmdRjmLcoj85pCLJW2SsPKHGPizn6VQajTWr6bV2+DQYsmPLXffdJRLsFLCHGCoqOAUHkk9gPWuK+ivaPRKLLFa8+LaFm8bIbCbRpl25NKXbI1xaTOKQTtaIwrO3noCOPUVoaRw1iJYS9uK0yhmv8TYfEBMjw9fZcgGzyJFxaiv+aynYhZQTycHcEcds+5r08sVs0/BPhHc9Wvec/e7hb3hIkvOqUVf9T2PH5U/xQX3wq0zaLLpi33G3RfKl3KBHclOFxSt6tmehOByo9MUF1oFBy3Wvh3JXLeuOnUIWHVFbkUkJIUepSTxg+nbt6C0ways1imXt3ctK5tNm83BPXrCjf61qFckIFluG/oR+HUEj92Mf3XX5mGK/zhNfXam+bzYpt227TDomhfD96DLaul8CA60dzEZJCtivmURxkdgMjvn0pMtptaZmd1nm10Xx8FI236/R0KTGYlx3I8plt9hwbVtOoCkqHoQeDUbgacGw2i3xX4sC1wo0eQCHmmWEoS4CMHcAOeOOaD7RZ7Yi1m1IgRk28gp/ChoBvBOSNvTrzQbUZhmLHajxmkNMtICG20DCUJAwAB2AFBkoFAoFAoFAoFAoFAoFAoFAoFAoFAoFAoFAoFAoFAoFB//Z')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(brfs3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(brfs3['5 dias']))
        col3.metric(label="10 dias", value=(brfs3['10 dias']))
        col4.metric(label="20 dias", value=(brfs3['20 dias']))
        col5.metric(label="30 dias", value=(brfs3['30 dias']))
        col6.metric(label="60 dias", value=(brfs3['60 dias']))
        col7.metric(label="90 dias", value=(brfs3['90 dias']))
        col8.metric(label="% Probabilidade", value=(brfs3['% Probabilidade']))
        
        base=yf.download('BRFS3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'RRRP3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAArCAMAAADluJ77AAAAwFBMVEX///8hW0qh1koGjKAATzvDzspMwIQASTOgsaseWkgJU0AASza1w74AUT4sX0/8/PwAg5mc1Dz09vWZ0zTw+OU/vX3L1NGOo5zs7+7d4+E5aFm/4oyl11PT29if1UT7/fnd78ROdWiAmJBui4FbxI0APSO209phgXZEb2Hk8tC54IHY7buS0Bj2+/DQ6q7G5Zqw3G7q9dvD59OS1bCAzqPP69vl9Oum3L7S5Oimy9Met29ZpLSDt8NGm6xyr7yVwMq8tFkQAAADuUlEQVRIia2WC3eiOhDHh5dAwstYCFC1VWvF9m7v7etud7ftfv9vdScJIVbBrfd0zhGSGH78ZzKZAGBsez61pze38BV2/tfYtu35eLL9Ctq384kt7GtocKloc2ym3mesmJVpj6qzC3G7E57a40sA5rufMUrjms8+oO6mk8n45gxbU6nsb4TFofU5CwltDO7Mlnrmk9tW2vzmFJjg+VyzJnPb1pG/F1Gbn58Isyza0mzNsudT9HOulvNEmOV7KubCFHB8gTrHExR2MiwMpbDp3XZ7+49MijH2L27vxTDzY23EPHLkDa6QdqmcvZ+ipEuzwGmkzeOaFtKo7mi+tLiDkeVufpxtv/VmcuTq6UkFiYb58j8WdbLDhZr+8Pj0+DywKWBJ29l0hb09GMBMvypMRPc5z/NRnn/vRbGFdsSNoA8GnTJLyPo5kpb/28OqQv0wCaAfpgfCBjv5qIX1OOr5ZvXikKc9MBNRjMKDho16hHmutWOEFAZGgaFVvJshwvCkZOVXfV6m8S4Mt6C3lxrU5CBF3VcCNfo+sJibvSQNE2vAXBFTwepfSBmR9d77h4zILLsa5Q94u3Yy52WAmFYB/QPLVRn7lD/i9UfmOE62T2FGYXyUpQvQ80+s1y+C5WTl3lquI90sj0pzu0L7hL9fjoShktL4WlDcQWxQWUgOtqUKihTm/AJ4zbK3dnAmxBB3WTBWBu5B6aEAvHuDGxhY6+ULXGMjezcsiaMxJYdlTOyALoMtWnWwMmuFSXczcRJWh1oOYTO/c7Q20iTjGuBNNyq/nxV+gMGyC1vMO9hrJr1sF0L4uepdPrKqP8DA0P3OUdbCfuvgAQQ92ki9XzUK42jSScPIC+9U8BxHJERV04+4kG4OS5BxlPAdWoYL0EqTYEzahR/r4ojfAIlI4TAmytbtg90AWZtvBPYuN8BrS8t+yGWOVrU6hRpeyGlBZzodzUi3X+SjMufekZS9XZthVpYM/rex8s9zTrQ0VVe8paKTqgFVSvR/qWylbX+QVfrijMZKS4JVSCw39THNSyiIKPYerqsoBJaVukiisMDjPAqHYXgM1rONSkXCgBGM/pKtK3xNVQiYJw5laGF+xWgyDEskbMk5RjAuJWzJI/FBEXAJK2rOPQlzYRElm2PKfPE5uOFRxBSMJusVREINb2GNF80AS1HqQ1PyDZCjbgIsVCK6UlmRAFsXUK3LHTcxlaMGmgoXJh6Gyeq5rBMLt0mDMcPTnwdQLXz8Gp7VSbKq8BLiPH9Rgoht2vwHMHBKDsAvDecAAAAASUVORK5CYII=')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(rrrp3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(rrrp3['5 dias']))
        col3.metric(label="10 dias", value=(rrrp3['10 dias']))
        col4.metric(label="20 dias", value=(rrrp3['20 dias']))
        col5.metric(label="30 dias", value=(rrrp3['30 dias']))
        col6.metric(label="60 dias", value=(rrrp3['60 dias']))
        col7.metric(label="90 dias", value=(rrrp3['90 dias']))
        col8.metric(label="% Probabilidade", value=(rrrp3['% Probabilidade']))
        
        base=yf.download('RRRP3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)
    
    elif tabs == 'MULT3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAQCAMAAACLBWmVAAAAjVBMVEX///8AAAAMDAx8fHxcXFw9PT3Q0NCxsbGPj4/q6upzc3NnZ2f49PSrbGxLS0sYGBijo6OhVVW6iYmIAADUubnu5OTj0tKHh4ff39/CwsIwMDCnYWHz7OzCmJibm5siIiKRKyuLFBSudHRUVFTHoaGYPj6bRUXbxcW0fX2eTU3QsbGMHByVNjZERETp29uPmG17AAABw0lEQVQ4ja2Ti3KjMAxFpbaGAiYBg83DBGhCEpI0/P/nrWRamj623ZmuZ5AY2T5z5WsDgEqt1TBZmyr47cgmnTc55M1Zm6dfskaj4nx/hPyQ281x/HqRbBOKAX1VFyxV//7jul6eKD4Bi9q72CLyRILibRXSvoDLj+gtxRV+gjVbigdgpJWXGVZR6j7CwtqJdMHJe7hjua9KOadyn0vSdAB5PjUpw3YYApRdLaBiHfXVwZAGRw92K/pNZhhXPQhE5PL0DJt4m0G2jQfoNXfic59F+woTq1mZYGUFVXAHcKXMsBIgQiixoJIAmcnjMFzgMgymyaSD3VOfGHRfwXyGRQShimuTS3ScJDREiHWsjOnh2ZhxNLGDeRiWa1h/B2N5Tllb3MB6aRcDTpLdfEzoJMLkJ1jEsAofvFtYw2ou0DszXmAhovweVtJ2gl3xXZu2SQe93YAa9cZOdoZVSAAHqxY3QaxvYDt0bkYY0FVaYHToZ2UmmI4ql1nDhtEE+vR17JTAjjJfFh9X7QwLC8TSXVpZI9Z3MsDWuQp6H6uUnlOq4kPz6SEFnnz7L19ucAQ3xeD9Bqld0hL+bTgD/tcQxV8m/gDYtR7eZk6x5gAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(mult3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(mult3['5 dias']))
        col3.metric(label="10 dias", value=(mult3['10 dias']))
        col4.metric(label="20 dias", value=(mult3['20 dias']))
        col5.metric(label="30 dias", value=(mult3['30 dias']))
        col6.metric(label="60 dias", value=(mult3['60 dias']))
        col7.metric(label="90 dias", value=(mult3['90 dias']))
        col8.metric(label="% Probabilidade", value=(mult3['% Probabilidade']))
        
        base=yf.download('MULT3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)    
    
    elif tabs == 'ALSO3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAALCAMAAADiFJvNAAAAt1BMVEX///+/xNgAGoHX2ufp6/KWn8DN0eDT3uCetryTrrTg5+n6/PzP297Kzt7Fytzd4OpWZqAAAHuHkbh/i7Xs8/TJ2960udFBVpgTNomuw8jn7e/I1diLqK8ARFkwc4CBoqkAUGJpkZtQg45dipS6zNA+eYV1l6Cfp8UNYnH7wIBjcqYDMIdcmqObvsSIs7muys46jJb+69n5nBb95c3+9OoAKoVzqLD7unNyfq0AJIMnQo4ADn00S5MC8UMnAAABnklEQVQokZWSbXeiMBCFbyBAIOXVAJp1daUou5YXa1trt/3/v2snqGf1nH5xTuDMZJKHexMAeMAMeNBQGloBPzCbKwhfSOFT766QP4EFIB7gLxH8UljKFVAF0PLxThTg1wLrETZ/RDBbax+bcYa+Mb9X2cJfjDCv3mxEUKOqDHlhWqubhWF0yXhh3vG55g0K+5QKD7N67Qvhkam1V5NDvax0UIkVfvv1FaxILhlLHUCl5amKUziTS0udn/8hcTv15wTbsixGbLssnD4BzZTgRRYitgzMnjQKqu0w9EOLLgfacey6a0F4fd6/vBqYlTUpD99KFm0ThqemRDlhls0NTKaRwwhGu+n/6Ia2xgH5LiCevIY9v+/fXwyMbB0d1yKbCUvs0qU6yqbFCMPHkdEab2d4qu9wGA5oSWM75Ld3tD/ZpM3bxv1rYPggfUYZL88wRMmEjqbXrUYfdBJ9q6mQO3wbxecxS1U0JViJ7BPsC29ZZhXcXED8VSQOSRqArvPgkbc8l9Be3Q3fwbjt0hlzcsPDcUTgTmTHcCFt2A3DP/KTIbD7SZ+cAAAAAElFTkSuQmCC')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(also3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(also3['5 dias']))
        col3.metric(label="10 dias", value=(also3['10 dias']))
        col4.metric(label="20 dias", value=(also3['20 dias']))
        col5.metric(label="30 dias", value=(also3['30 dias']))
        col6.metric(label="60 dias", value=(also3['60 dias']))
        col7.metric(label="90 dias", value=(also3['90 dias']))
        col8.metric(label="% Probabilidade", value=(also3['% Probabilidade']))
        
        base=yf.download('ALSO3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)         
    
    elif tabs == 'CYRE3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAwCAMAAACMqWyjAAAAkFBMVEX///8AAADjzMzHkpTFxcWmEBKnGBuxU1G7cHGHh4dDQ0PQnp+oLSz39/f7+/vn5+fR0dHGiIWmFxZ5eXmZmZng4OCyXVytra0xMTHt7e2ioqLY2NiqIyVzc3NhYWEeHh62trZTU1OoQkTt396iCQioLzLZt7eyaGmWAACjAACQkJBpaWmtOzg7OzsZGBkLCwtEi7u4AAABfUlEQVRIie2U23LCIBBAlxZjqbkZQCQkmqitNW31//+uQC6iTn0xnekDZyazBNgTNoEAeDye/000nuppM5mNpNoudmGYvb2PoEr2H4ed5rALx9CNyOz5zPZR2SYogpbi8NT1iUYIWkaibmIAXMtmxRqqAEyDkU/gpMZxP1c5smnxtWgpJq0sWqYmMAUl1ZELSBCAQjorXeqOKgb8PeSjxpUNuyLsZLVo7zlIJHUuWBmsSCczq33t07E4urLsSqZQPAxSaoOV1XkriyJXRgCpO7J8fR60S9P5TF96YZAeMSauTAog5I6MOTIgdmlyKUqbkq6ThLmyPK+IM/9GhpFzUNs3bco8mTd5U2aZcO7UeSMD1H0AeSFLzTPsB4BeFoMyU506p8G1LEXcBI4vZEC1ID3Z2gBbaQVlZOefZcV03tLvM+ArgjGrTYsgHIFkqNJZtFYE0TynRNpYp9hWiBGRg6zIDEF2PgEQc37vDxf/NjB/Gdg/fDY9Ho/H85f8AI/rGd3kbnj+AAAAAElFTkSuQmCC')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(cyre3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(cyre3['5 dias']))
        col3.metric(label="10 dias", value=(cyre3['10 dias']))
        col4.metric(label="20 dias", value=(cyre3['20 dias']))
        col5.metric(label="30 dias", value=(cyre3['30 dias']))
        col6.metric(label="60 dias", value=(cyre3['60 dias']))
        col7.metric(label="90 dias", value=(cyre3['90 dias']))
        col8.metric(label="% Probabilidade", value=(cyre3['% Probabilidade']))
        
        base=yf.download('CYRE3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)  
    
    elif tabs == 'AZUL4':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAABECAMAAAAPzWOAAAABU1BMVEX///8KGj8AAC4gJ0QAADUaZbHJ2O0PHUHd3eEAACvf5vEgZ7IAACYAACAAADOgutqqwN2TlqGcn6kAEDsAWq0AFDzF0eYACjgvbrXx8fMAX6+NkJyVr9XA4b9ItVf6/fbZ56T1+eGs4PSa3Phqxacfqw2Wzd+vst240Ta0wqjy8PrGx8x7f41KweoAtOgAttgTuMYKoNVHTqZhc5VkbqpRs9V3zNr/+95iZnhTWadQaKgZq849w7/wuxq9XLH99eVRt8l3yZhYwbTau2LdqkTx4acAAAnrx12gxjiKxTCDxJSTvpDD4u48Q12l0F5hqaQAmufMobBdy+Aie7HXnUjkoEBUk6/MtM+EL5CKQZZ3gZrwoSX/oACFAIOTKIfkJwHnXBDbyLh6nMvcxdmodbAWlajSZ2+wu8z92tOSfplqm8AAABdRgsDvXD71JAD0rqXylogqKI1FAAABuUlEQVRYhe2S61PTQBDA9y5JL0mbw1xaQtqoID6AixVQYmutWB4KKIjlrfigiqjUx///yW1axpE5nPGLn+6XyVwuu/O73ZsF0Gg0Go1G89+4fOUqjI79JcEXvq2OCOFn67Xx6zdu3pqYnLrQIT3TSdQhzr1svV29Mz0ze/feXHr/AkktYCRUhwihA0m1OlOvP2g8bD5yVYkRZQGjEr/sAZHrRvjfdYH1JfPpY5TM1lsLrcWlZZVEcFMEQa1Xkuc4DqVPhovFIYChYjFn9CVPm82V1TRNW2vP5hrPVZL1EsfXwbOTEjMMxk6HrTxKLlnWmQTZ2EDJi8bm5kuVwy6UaiBMLvo7Rgoip5BA1G63t7Z3dpV3Vwm5hMghRuYw0QGqSgD29g9evT4USklICOs9BRwV2+k5ziT5c5I3b9+9PzxSOSRlIaWUszABm5OsK2wnBuick3z4eHz8SUYqSS0IEymloDgqQYkYCXJSHsnHHWvkTwl8/vJV2QtEnull8nVeECaCVZ3KLgrKXaucI4OJzfj2XTlneAsVv39VsuKfCD+jYkdxt5Nz49jFze/cHz/VDo1Go9FoNP/ML7STMOnJt6LAAAAAAElFTkSuQmCC')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(azul4['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(azul4['5 dias']))
        col3.metric(label="10 dias", value=(azul4['10 dias']))
        col4.metric(label="20 dias", value=(azul4['20 dias']))
        col5.metric(label="30 dias", value=(azul4['30 dias']))
        col6.metric(label="60 dias", value=(azul4['60 dias']))
        col7.metric(label="90 dias", value=(azul4['90 dias']))
        col8.metric(label="% Probabilidade", value=(azul4['% Probabilidade']))
        
        base=yf.download('AZUL4.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)               
    
    elif tabs == 'PETZ3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/jpeg;base64,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')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(petz3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(petz3['5 dias']))
        col3.metric(label="10 dias", value=(petz3['10 dias']))
        col4.metric(label="20 dias", value=(petz3['20 dias']))
        col5.metric(label="30 dias", value=(petz3['30 dias']))
        col6.metric(label="60 dias", value=(petz3['60 dias']))
        col7.metric(label="90 dias", value=(petz3['90 dias']))
        col8.metric(label="% Probabilidade", value=(petz3['% Probabilidade']))
        
        base=yf.download('PETZ3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)  
    
    elif tabs == 'LWSA3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAPCAMAAAB5hdnbAAAAzFBMVEX////4+PnuAEEkLzoAFiZfZWztADv95+vuDEEpMz0nMTzxTGztADgAECLtADUXJTHuFkWcn6MeKjb3orDs7e6Lj5NASVKWmp4NHiztADH70Nf+7PDR09WlqKw5QkxvdHr2laTtACv5tsLvJ1G5vL6xs7YvO0XjQmX6w8z1hpz1jZ/wMVrxP2PvF0vzdIrf4eIAABqzDzvza4N2KkJLNkTVJ0wTNz/yYHv4rLn82+OmOFOwhZEVLDZLU1t/PlN7gIa0ME0AABEAJS5hWmbI903PAAACHUlEQVQ4jdWTW3vaMAyG5SY2soE4zRnICQzpGg7ZWFfo1q3d9v//02QI3brn2VWvphsrcp43Xz5JwLSs4C0x8HF4yZnr8LfBrv4fWBQnjWz40lZWvJEy4RHkvHSc0harsukAZtv1Dd2/M+YWoF2PJmITWpjvX3nedjfrYSzRTqADxy0AUpdSrd0OVu/ppGIKqc5WAAsPPxBzJ7wF7D1EgThpTzAhhC82PWyZSRlf80AlwKQMqmsKBl1KB3ekA3lm5e8RPxbANogzIuAu3Al/ZGHrsG6v/Mn0DEsDTV+GRrmMuTJ55Ukpx8BK1TAwvrnjMBjhBqYj3NPdECez2dmzWojjGRYHWU4F7rhR5DpPF063LIrCwqBydD4V/qd7F0Ihags7LI5Hgj30sMVIhK9gTwTrsiDuWfE4G4/HysJWOrgOBX6+z/I9elOYer6Yz+eemE//BeMn2EVZRBauVquTsi5w+AHxy2MQb30PCIaHY2iDDf6GvXiWschVvWe5Pmn8qggGiXO3RRMFj98QD3Dx7I85++0ZdbNJi+rUTSWDJ7KqYJ1WyTI/K4PYUnbA759xdKSRQ+pmXdftg+2maetb8dJNVmpFc6bsnMWu6uesDJTOtFLfrczsGScLSH+scT6g590EabjEPLTdtSl6pI81ZdVvQHnegOIrbUBJG9BVpZRNwlNb5TeG3o5+GtOe/i4cGmPWQ1LTHoYbY4Y1g18EBDT8NzB4VAAAAABJRU5ErkJggg==')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(lwsa3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(lwsa3['5 dias']))
        col3.metric(label="10 dias", value=(lwsa3['10 dias']))
        col4.metric(label="20 dias", value=(lwsa3['20 dias']))
        col5.metric(label="30 dias", value=(lwsa3['30 dias']))
        col6.metric(label="60 dias", value=(lwsa3['60 dias']))
        col7.metric(label="90 dias", value=(lwsa3['90 dias']))
        col8.metric(label="% Probabilidade", value=(lwsa3['% Probabilidade']))
        
        base=yf.download('LWSA3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)  
    
    elif tabs == 'CVCB3':
        st.title("Preço Previsto do Ativo")
        st.write('Atualizado em:', today)
        st.image('data:image/png;base64,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')
        st.write('{}'.format(tabs))
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.metric(label="Fechamento D-1", value=(cvcb3['Fechamento Anterior']))
        col2.metric(label="5 dias", value=(cvcb3['5 dias']))
        col3.metric(label="10 dias", value=(cvcb3['10 dias']))
        col4.metric(label="20 dias", value=(cvcb3['20 dias']))
        col5.metric(label="30 dias", value=(cvcb3['30 dias']))
        col6.metric(label="60 dias", value=(cvcb3['60 dias']))
        col7.metric(label="90 dias", value=(cvcb3['90 dias']))
        col8.metric(label="% Probabilidade", value=(cvcb3['% Probabilidade']))
        
        base=yf.download('CVCB3.SA',start= start_date,end= end_date, progress=False) 
        
        # Bollinger Bands
        indicator_bb = BollingerBands(base['Close'])
        bb = base
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
    
        # Moving Average Convergence Divergence
        macd = MACD(base['Close']).macd()
    
        # Resistence Strength Indicator
        rsi = RSIIndicator(base['Close']).rsi()
        
        st.title("Evolução do Ativo")
        
        
        # Plot the prices and the bolinger bands
        st.write('Preço de Fechamento x  Bandas de Bolinger')
        st.line_chart(bb)
    
        progress_bar = st.progress(0)
    
        # Plot MACD
        st.write('Média Móvel Convergente e Divergente - MACD')
        st.area_chart(macd)
    
        # Plot RSI
        st.write('Índice de Força Relativa ')
        st.line_chart(rsi)                                                                                                          
                                                                                          
    
    
    
    st.header('Isenção de Resposabilidade Legal:')
    st.warning("As informações fornecidas pela QUANTI MIND e não devem ser interpretadas como uma oferta ou solicitação para a compra ou venda de qualquer instrumento financeiro ou o fornecimento de uma oferta para fornecer serviços de investimento. As informações, opiniões e comentários não se enquadram no escopo dos serviços de assessoria de investimentos. Os serviços de assessoria de investimento são prestados de acordo com o contrato de assessoria de investimento, celebrado entre as instituições intermediárias, sociedades gestoras de carteiras, bancos de investimento e os clientes. As opiniões e comentários refletem o resultado de simulações de modelos matemáticos. As informações discutidas neste relatório podem envolver riscos significativos, podem não ter liquidez e podem não ser adequados para todos os investidores. Portanto, tomar decisões com relação às informações deste relatório pode causar resultados inadequados e perdas financeiras.", icon="⚠️")
    
    

        
