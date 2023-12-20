import React from 'react'
import './About.css'
import axios from 'axios'
import { useEffect , useState } from 'react'

var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };


const baseURL = "http://127.0.0.1:8000/about"
function About() {

    const [aboutData , setAboutData] = useState('')
    useEffect(()=>{

        fetch(baseURL , requestOptions)
        .then(response => response.json())
        .catch(error=> console.log('error', error))
        .then(result => setAboutData(result))
    },[])

    
    

    const ed = aboutData.education?.map((item)=>(
        //    console.log(item.title)
            <>
               <li>
                <h5>2018 - 2022</h5>
                <h4>Bachelor Degree Computer Science</h4>
                <h4>Dr. A. P. J. Abdul Kalam Technical University</h4>
                </li> 
            </>
        ))

    const ex = aboutData.work_experience?.map((item)=>{
        // console.log(item)
        <>
            <li>
                <h4>1</h4>
            </li>
        </>
    })
    

    

  return (
    <div className='about-container'>
    <div className="container">
        <div className="left_Side">
        <div className="profileText">
            <div className="imgBx">
                <img className="photo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/2048px-Default_pfp.svg.png"/>
            </div>
            <br/>
            
        </div>

        <div className="contactInfo">
            <h3 className="title">Contact Info</h3>
            <ul>
                <li>
                    <span className="icon"><i className="fa fa-phone" aria-hidden="true"></i></span>
                    <span className="text">{aboutData.phone}</span>
                </li>
                <li>
                    <span className="icon"><i className="fa fa-envelope-o" aria-hidden="true"></i></span>
                    <span className="text">{aboutData.email_id}</span>
                </li>
                <li>
                    <span className="icon"><i className="fa fa-globe" aria-hidden="true"></i></span>
                    <span className="text">{aboutData.website}</span>
                </li>
                <li>
                    <span className="icon"><i className="fa fa-linkedin" aria-hidden="true"></i></span>
                    <span className="text">{aboutData.linkedin_url}</span>
                </li>
                <li>
                    <span className="icon"><i className="fa fa-map-marker" aria-hidden="true"></i></span>
                    <span className="text">India</span>
                </li>
            </ul>
        </div>
        <div className="contactInfo education">
            <h3 className="title">Education</h3>
            <ul>
                {ed}
            </ul>
        </div>
        
            </div>
            <div className="right_Side">

                <div className='about'>
                    <h1 className='title-name'>{aboutData.name}</h1>
                </div>
                <div className="about">
                    <p>{aboutData.desc}</p>
                </div>
                <div className="about">
                    <h2 className="title2">Experience</h2>
                    <div className="box">
                        {ex}
                    </div>
                </div>
                
                <div className="about interest">
                    <h2 className="title2">Interests</h2>
                    <ul>
                        <ol> <button className="skill-btn">Reading</button></ol>
                    </ul>
                </div>
            </div>
    </div>
    </div>
  )
}

export default About