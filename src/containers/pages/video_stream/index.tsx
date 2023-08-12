import React, { useEffect, useRef, useState } from 'react';

const VideoStream: React.FC = () => {
  const [image, setImage] = useState("")
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  
  const drawOnCanvas = (tools: any[]) => {
    if (canvasRef.current) {
      const context = canvasRef.current.getContext('2d');
      if (context) {
        // Clear the canvas before drawing new tools
        context.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);

        tools.forEach(tool => {
          context.fillStyle = tool.color;
          if (tool.type === 'rectangle') {
            console.log('drawing rectangle',tool)
            context.fillRect(tool.x, tool.y, tool.w, tool.h);
          } else if (tool.type === 'text') {
            context.fillText(tool.text, 20, 20);
          }
        });
      }
    }
  }

  const captureFrame = () => {
    if (videoRef.current) {
      const canvas = document.createElement('canvas');
      canvas.width = videoRef.current.videoWidth;
      canvas.height = videoRef.current.videoHeight;
      const context = canvas.getContext('2d');
      if (context) {
        context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
        const frame = canvas.toDataURL('image/png');
        //console.log(frame); // log the frame data
        fetch('http://localhost:8000/api/monitoreo/image-processor', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ frame })
        })
        .then(response => response.json())
        .then(data => {
          //console.log('Success:', data);
          //console.log(data.tools)
          
          setImage(data.image)
          drawOnCanvas(data.tools); // draw the new tools
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      }
    }
  };

  useEffect(() => {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
          }
        })
        .catch(err => console.log(err));
    }

    const intervalId = setInterval(captureFrame, 1000); // capture frame every second

    // Clean up function
    return () => {
      clearInterval(intervalId);
      if (videoRef.current && videoRef.current.srcObject) {
        const tracks = (videoRef.current.srcObject as MediaStream).getTracks();
        tracks.forEach((track) => track.stop());
      }
    };
  }, []);

  return (<>
    <div className='flex items-center h-screen'>
      <div className='w-full md:w-1/2 m-auto'>
        <div style={{position: 'relative'}}>
          <video ref={videoRef} autoPlay={true} style={{position: 'absolute'}}/>
          <canvas ref={canvasRef} style={{position: 'absolute'}} />
        </div>
      </div>
    </div>
  </>);
};

export default VideoStream;
