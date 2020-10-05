import {apiInstance} from './instance'

export function createInvite() {
    console.log("Request Create intvite")
    const path = "/connection/new"
    return apiInstance.get(path)
}

export function checkActive(connectionId) {
    const path = `/connection/${connectionId}/active`

    return apiInstance.get(path)
}
