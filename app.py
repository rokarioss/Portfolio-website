from flask import Flask, render_template, url_for, jsonify 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

JOBS = [
    {
        'id':1, 
        'title':'Backend developer',
        'location':'Abuja, Nigeria',
        # 'Wages/Hour':'negotiable',
        'member': 'Ajiri "rokari" iyelobu',
        'github': 'https://github.com/rokarioss'
    }, 
    # {
    #     'id':2, 
    #     'title':'Data Scientist',
    #     'location':'Abuja, Nigeria',
    #     # 'Wages/Hour':'negotiable',
    #     'member': 'anosike ugochukwu'
    # },
    {
        'id':3, 
        'title':'Front End Engineer',
        'location':'Uke, Nigeria',
        # 'Wages/Hour':'negotiable',
        'member': 'Daniel "kng-koder" fori',
        'github': 'https://github.com/DFori'

    },
    {
        'id':4, 
        'title':'Fullstack Developer',
        'location':'remote',
        # 'Wages/Hour':'negotiable',
        'member': 'Aigbona Benjamin "bencool"',
        'github':'https://github.com/aigbonabenjamin'
    }
    
]

SERV = [
    {
        'id':1,
        'title':'Website development',
        'price':'Negotiable',
        'duration':'Depending on customer terms'
    },
    {
        'id':2,
        'title':'Back-end data-base management',
        'price':'Negotiable',
        'duration':'Depending on payment'
    },
    {
        'id':3,
        'title':'Cyber Security & IT-support services',
        'price':'Negotiable',
        'duration':'Depends on price'
    }
]
@app.route('/')

def index():
    return render_template('landing.html',
     jobs= JOBS,
     company_name= 'Code-crusaders',
     services= SERV
     )
@app.route('/api')
def api_call():
    return 'this is the api webpage'


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/api/services')
def list_services():
    return jsonify(SERV)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)