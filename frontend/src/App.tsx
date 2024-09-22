import { FormEvent, useState } from "react";
import { toast, ToastContainer } from "react-toastify";
import ladybugIcon from "./images/ladybug.png";

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  // const uploadHandler = async (e: FormEvent) => {
  //   e.preventDefault();
  //   try {
  //     const formData = new FormData();
  //     formData.append("inputFile", "hey");
  //     const res = await fetch("http://127.0.0.1:8000/upload", {
  //       method: "POST",
  //       body: formData,
  //     });
  //     console.log(res);
  //   } catch (err) {
  //     console.log(err);
  //   }
  // };

  //   const onChangeHandler = (event: any) => {

  // };

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    if (selectedFile != null) {
      const formData = new FormData();
      formData.append("cow", "name");
      formData.append("video", selectedFile);

      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });
      console.log(res.body);
    }
  };

  return (
    <>
      <ToastContainer />
      <div className="upload">
        <div
          style={{ backgroundColor: "#0e5d5b" }}
          className="font-bold h-24 flex items-center"
        >
          <img className="h-16 ml-12" src={ladybugIcon} />
          <div className="text-white text-5xl font-semibold m-4 ">PestNet</div>
        </div>
        <div
          style={{
            background:
              "linear-gradient(180deg, rgb(26, 191, 73) 0%, rgb(175.79, 224.62, 234.39) 50%)",
            height: "calc(100vh - 96px)",
          }}
          className="p-12"
        >
          <div className="bg-white h-full w-full flex justify-center items-center">
            <div className="flex flex-col items-center w-[40%] text-center">
              <p style={{ color: "#453030" }} className="text-4xl my-3">
                Upload a .MP4 video of the pest/plants here
              </p>
              <p className="my-3 text-2xl">
                Drag and drop video files to find what pests are in your plants
                and how to deal with them
              </p>
              <button
                style={{ backgroundColor: "#1abf49" }}
                className="text-white px-8 py-3 rounded-full my-3 text-xl"
              >
                Select a file
              </button>
            </div>
          </div>
        </div>
      </div>
      <div>
         {/* Conditionally render the selected image if it exists */}
        {
        // selectedFile && (
        //   <div>
        //     {/* Display the selected image */}
        //     <img
        //       alt="not found"
        //       width={"250px"}
        //       src={URL.createObjectURL(selectedImage)}
        //     />
        //     <br /> <br />
        //     {/* Button to remove the selected image */}
        //     <button onClick={() => setSelectedImage(null)}>Remove</button>
        //   </div>
        // )
        } 
        
        {/* Input element to select an image file */}
        {/* <form onSubmit={uploadHandler} encType="multipart/form-data">
          <input
            type="file"
            name="myImage"
            // Event handler to capture file selection and update the state
            onChange={(event) => {
              if (event.target.files == null) {
                toast.error("Please upload a file!");
              } else if (event.target.files[0].type.split("/")[0] != "image") {
                toast.error("Please upload an image!");
              } else {
                console.log(event.target.files[0]); // Log the selected file
                setSelectedImage(event.target.files[0]); // Update the state with the selected file
              }
            }}
          />
          <input type="submit" />
        </form> */}
        <div>
          <form onSubmit={handleSubmit}>
            <label>
              Upload a file: <br />
              <br />
              <input
                type="file"
                name="file"
                onChange={(event) => {
                  if (event.target.files != null) {
                    setSelectedFile(event.target.files[0]);
                    // console.log(event.target.files[0]);
                  }
                }}
              />
            </label>
            <br />
            <br />
            <button type="submit">Upload</button>
          </form>
        </div>
      </div>
    </>
  );
}

export default App;
