import React from 'react'
import './Dashboard.css'
function Dashboard() {
  return (
    <section className="hero-section">
      <div className="hero">
        <h2>Hi! My Name is Rachit!</h2>
        <p>
          A <span className='into-text'>Developer/Engineer</span> by <span className='into-text'>Profession/Hobby</span>
        </p>
        <div className="buttons">
          <a href="#" className="join">About me?</a>
          <a href="#" className="learn">Contact Me?</a>
        </div>
      </div>
      {/* <div className="img">
        <img src="hero-bg.png" alt="hero image"/>
      </div> */}
    </section>
  )
}

export default Dashboard