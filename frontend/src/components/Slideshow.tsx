import { Carousel } from "flowbite-react";
import { BugDetails } from "../interfaces.tsx";
function capitalizeFirstLetter(str: string) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}
export default function Slideshow({ data }: { data: BugDetails[] }) {
  return (
    <>
    <div style={{ height: "calc(100vh - 192px)" }} className="w-full">
          <Carousel slide = {false} id="hey">
            {data.map((e, i) => {
              return (
                <div
                  key={i}
                  className="duration-700 ease-in-out"
                  data-carousel-item
                >
                  <div className="relative block h-full px-20 text-black">
                    <div className="absolute right-2 top-2 font-bold">
                      {i}/{data.length}
                    </div>
                    <h1 className="font-bold text-center py-3 text-3xl">
                      {e.bug}
                    </h1>
                    <div className="grid gap-2">
                      <div className="text-2xl bg-[#ADE0E8] rounded-lg p-3">
                        <h1 className="text-center font-bold">
                          Preventive Measures
                        </h1>
                        {capitalizeFirstLetter(e.description)}
                      </div>
                      <div className="text-2xl bg-[#ADE0E8] rounded-lg p-3">
                        <h1 className="text-center font-bold">Timestamps</h1>
                        {e.timestamp.map((ee, ii) => {
                          return (
                            <p key={ii}>
                              {"\u2022"} {ee}
                            </p>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </Carousel>
      </div>
    </>
  );
}
