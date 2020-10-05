import React from 'react'
import {useQRCode} from 'react-qrcodes'

const QrCode = ({url}) => {
    const [inputRef] = useQRCode({
        text: url,
        options: {
            type: 'image/jpeg',
            quality: 0.3,
            level: 'M',
            margin: 3,
            scale: 4,
            width: 200,
            color: {
                dark: '#000000',
                light: '#FFFFFF',
            },
        },
    });

    return <img ref={inputRef}/>
}

export default QrCode
