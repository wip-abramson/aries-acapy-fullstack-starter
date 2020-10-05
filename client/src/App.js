import React from 'react';
import logo from './logo.svg';
import './App.css';
import Invite from './Invite';
import {checkActive} from "./api/connections";
import ConnectionPage from './ConnectionPage'
function App() {

  let [connectionId, setConnectionId] = React.useState(null)
    let [connectionActive, setConnectionActive] = React.useState(false)

    React.useEffect(() => {

        if (connectionId && !connectionActive) {
            const interval = setInterval(() => {
                checkActive(connectionId).then(response => {
                    console.log("ACTIVE", response.data.active)
                    if (response.data.active) {
                        setConnectionActive(response.data.active)
                        return () => clearInterval(interval);
                    }

                })
            }, 2000);
            return () => clearInterval(interval);
        }


    }, [connectionId, connectionActive])

  return (
    <div className="App">
      <header className="App-header">
      {/*<img class="logo_text" src="logo_text.png" alt="Logo"></img>*/}
      <div class="disclaimer">Experimental</div>

          <div><h2>OpenMined Aries Starter Frontend</h2></div>


          {
              connectionActive ?

                  <ConnectionPage connectionId={connectionId}/>
                  : <>
                      <h3>Scan this QrCode to make a connection:</h3>
                      <Invite setConnectionId={setConnectionId}/>
                      <p className="instructions">
                          You should be able to use any of the following apps:
                          <ul>
                              <li>Trinsic</li>
                              <li>esatus</li>
                              <li>Connect.Me</li>
                          </ul>
                          <b>Make sure to set your network to the Sovrin Staging Network.</b>
                          Once you connect, you will be redirected to the appropriate page. If connection times out, try
                          refreshing the page and try again.
                      </p>
                  </>
          }


      </header>
    </div>
  );
}

export default App;
