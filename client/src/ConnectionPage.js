import React from 'react'

const ConnectionPage = ({connectionId}) => {

    return (<div className="connection-page">

        <h1>Congratulations, you now have a connection with {connectionId}</h1>
        <div className="main-text">
            <p>The rest is up to you. Using this connectionId you can engage in any number of protocols with their agent. Such as:
                <ul>
                    <li>Issuing them a credential</li>
                    <li>Verifying some attributes from them</li>
                    <li>Simply using this ID as a primary key for the application you are developing, enabling sign on through the authentcation as this identifier (Scanning the QrCode)</li>
                    <li>Using custom protocols such as sending attachments</li>
                </ul>
                When designing SSI applications, it is important to consider which actor is veiwing this client. Is it the credential holder, authenticating with the application in order to access a service. Or is it an issuer/verifier using the application in order to request verifications or issue credentials to certain connections.
            </p>
            <h3>If you need any help you can check out the tutorials in the <a href="https://github.com/OpenMined/PyDentity" target="_blank">PyDentity repository</a> or reach out on the <a href="https://blog.openmined.org/how-to-get-involved-into-openmined/" target="_blank">OpenMined slack</a>.</h3>

        </div>

        <h2>Play, Learn, Experiment. Have fun! Build something cool :)</h2>
    </div>)
}

export default ConnectionPage
