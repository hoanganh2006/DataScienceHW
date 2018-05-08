import numpy as np

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

engine=create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")

session=Session(bind=engine)

Base = automap_base()

Base.prepare(engine, reflect=True)

Samples = Base.classes.samples
Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/names')
def names():
    samples_query = session.query(Samples)
    samples = pd.read_sql(samples_query.statement, samples_query.session.bind)
    names_list=list()
    for i in samples.to_dict().keys():
        names_list.append(i)
    names_list =names_list[1:]
    return(jsonify(names_list))    

@app.route("/otu")
def otu():
    otu_query = session.query(OTU)
    otu = pd.read_sql(otu_query.statement, otu_query.session.bind)
    descriptions=otu.lowest_taxonomic_unit_found
    return(jsonify(descriptions.to_dict()))  

@app.route("/metadata/<sample>")
def metadata(sample):
    sampleID=int(sample.split("_")[1])
    metadata_query = session.query(Metadata).filter(Metadata.SAMPLEID==sampleID)
    metadata = pd.read_sql(metadata_query.statement, metadata_query.session.bind)
    return(jsonify(metadata.to_dict()))   

@app.route("/wfreq/<sample>")
def wfreq(sample):
    sampleID=int(sample.split("_")[1])
    wfreq_query = session.query(Metadata).filter(Metadata.SAMPLEID==sampleID)
    wfreq = int(pd.read_sql(wfreq_query.statement, wfreq_query.session.bind)['WFREQ'])
    return(jsonify(wfreq))

@app.route("/samples/<sample>")
def samples(sample):
    samples_query = session.query(Samples)
    all_samples = pd.read_sql(samples_query.statement, samples_query.session.bind)
    data=all_samples[['otu_id',sample]]
    data=data.loc[data[sample]>0]
    data.columns=['otu_id','samples']
    data=data.sort_values('samples',ascending=False)
    otu_ids=[]
    samples=[]
    for i in range(0,len(data)):
        otu_ids.append(str(data['otu_id'].iloc[i]))
        samples.append(str(data['samples'].iloc[i]))
    newdict={
        "otu_id":otu_ids,
        "samples":samples
    }

    return(jsonify(newdict))

@app.route("/samples/<sample>")
def samples(sample):
    samples_query = session.query(Samples)
    all_samples = pd.read_sql(samples_query.statement, samples_query.session.bind)
    data=all_samples[['otu_id',sample]]
    data=data.loc[data[sample]>0]
    data.columns=['otu_id','samples']
    data=data.sort_values('samples',ascending=False)
    otu_ids=[]
    samples=[]
    for i in range(0,len(data)):
        samples.append(str(data['samples'].iloc[i]))
        otu_ids.append(str(data['otu_id'].iloc[i]))  
    dict1={
        "otu_id":otu_ids,
        "samples":samples
    }
    otu_query = session.query(OTU)
    otu = pd.read_sql(otu_query.statement, otu_query.session.bind)
    otu_ids_2=[]
    descriptions=[]
    for i in range(0,len(data)):
        otu_ids_2.append(str(otu.otu_id.iloc[i]))
        descriptions.append(str(otu.lowest_taxonomic_unit_found.iloc[i]))
    dict2={
        "otu_id":otu_ids_2,
        "description":descriptions
    }
    df1=pd.DataFrame.from_dict(dict1)
    df2=pd.DataFrame.from_dict(dict2)
    merged=pd.merge(df1,df2,how='inner',on='otu_id')
    otu_ids_final=[]
    samples_final=[]
    descriptions_final=[]
    for i in range(0,len(merged)):
            otu_ids_final.append(merged.otu_id.iloc[i])
            samples_final.append(merged.samples.iloc[i])
            descriptions_final.append(merged.description.iloc[i])
    dictfinal={
        "otu_id":otu_ids_final,
        "samples":samples_final,
        "description":descriptions_final
    }
    return(jsonify(dictfinal))

if __name__ == "__main__":
    app.run()
    raise NotImplementedError()




