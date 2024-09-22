import { FormEvent, useEffect, useState } from "react";
import { toast, ToastContainer } from "react-toastify";
import ladybugIcon from "./images/ladybug.png";
import LoadingAnimation from "./components/LoadingAnimation";
import Slideshow from "./components/Slideshow";
import { BugDetails } from "./interfaces";
import ReactPlayer from "react-player";
import checkmark_icon from "./images/checkmark_icon.png";

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isFileSelected, setIsFileSelected] = useState(false);
  const [loader, setLoader] = useState(false);
  const [isSlidesOn, setIsSlidesOn] = useState(false);
  const [data, setData] = useState<Array<BugDetails>>([]);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);

  useEffect(() => {
    setData([{"bug": "Caterpillar", "timestamp": ["0:13-0:15-0:15", "0:23-1:19-1:19"], "description": "remove caterpillars and eggs where discovered and put them in soapy water; spray at them directly with soapy water, vinegar mixture, or insecticide"}, {"bug": "Beetle", "timestamp": ["0:12-0:13-0:13"], "description": "sprinkle Diatomaceous earth (keep soil dry); spray or pour soapy water, vinegar water, or boiling water"}]);
  }, []);

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    if (selectedFile != null) {
      setLoader(true);
      try {
        const formData = new FormData();
        formData.append("cow", "cow");
        formData.append("video", selectedFile);
        const res = await fetch("http://127.0.0.1:8000/upload", {
          method: "POST",
          body: formData,
        });
        const output = await res.json();
        console.log(output["insects"]);
        console.log("API Output:", output);
        if (Array.isArray(output["insects"])) {
          setData(output["insects"]);
        } else {
          toast.error("Unexpected response format from API");
          setData([]);  // Reset data to avoid errors
        }
        setLoader(false);
        setIsSlidesOn(true);
        setVideoUrl(URL.createObjectURL(selectedFile));
      } catch (err) {
        toast.error("There is an error");
        setLoader(false);
      }
    }
  };

  return (
    <>
      <ToastContainer />
      {/* Header */}
      <div
        style={{ backgroundColor: "#0e5d5b" }}
        className="font-bold h-24 flex items-center"
      >
        <img className="h-16 ml-12" src={ladybugIcon} alt="Ladybug Icon" />
        <div className="text-white text-5xl font-semibold m-4">PestNet</div>
      </div>
      {/* Main content */}
      <div
        style={{
          background: "linear-gradient(180deg, rgb(26, 191, 73) 0%, rgb(175.79, 224.62, 234.39) 50%)",
          height: "calc(100vh - 96px)",
        }}
        className="p-12"
      >
        <div className="bg-white h-full w-full flex items-center justify-center">
          {!loader && !isSlidesOn && (
            <div className="flex flex-col items-center w-[40%] text-center">
              <p style={{ color: "#453030" }} className="text-4xl my-3">
                Upload a .MP4 video of the pest/plants here
              </p>
              <p className="my-3 text-2xl">
                Find what pests are in your plants and how to deal with them
              </p>
              <form
                className="flex flex-col items-center"
                onSubmit={handleSubmit}
                encType="multipart/form-data"
              >
                <label
                  htmlFor="file-upload"
                  className="text-white px-8 py-3 rounded-full my-3 text-xl text-center inline-block bg-[#1abf49] cursor-pointer hover:bg-green-700"
                >
                  Select a File
                </label>
                <input
                  id="file-upload"
                  type="file"
                  name="file"
                  className="hidden"
                  onChange={(event) => {
                    if (event.target.files && event.target.files[0]) {
                      if (event.target.files[0].type.split("/")[0] !== "video") {
                        toast.error("Please upload a video!");
                      } else {
                        setSelectedFile(event.target.files[0]);
                        setIsFileSelected(true);
                      }
                    } else {
                      toast.error("Please upload a file!");
                    }
                  }}
                />
                
                  <button
                    type="submit"
                    className="font-bold"
                  >
                    Submit
                  </button>
                
              </form>
            </div>
          )}
          {loader && (
            <div className="mr-16">
              <LoadingAnimation />
            </div>
          )}
          {isSlidesOn && (
            <div className="h-full w-full grid grid-cols-2">
              <div className="h-full w-full flex justify-center items-center">
                {videoUrl && (
                  <ReactPlayer
                    url={videoUrl}
                    controls={true}
                    width="100%"
                    height="100%"
                  />
                )}
              </div>
              {data.length > 0 ? (
                <Slideshow data={data} />
              ) : (
                <div className="flex flex-col justify-center items-center">
                  <img className="size-56 mb-4" src={checkmark_icon} alt="Checkmark" />
                  <p className="text-2xl">No pests detected!</p>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default App;