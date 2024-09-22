import { BugDetails } from "../interfaces.tsx";
export default function Slideshow({ props }: { props: BugDetails[] }) {
  return (
    <>
      <div
        id="default-carousel"
        className="relative w-full"
        data-carousel="static"
      >
        {/* <!-- Carousel wrapper --> */}
        <div
          style={{ height: "calc(100vh - 192px)" }}
          className="relative
         overflow-hidden rounded-lg"
        >
          {props.map((e, i) => {
            return (
              <div
                key={i}
                className="hidden duration-700 ease-in-out"
                data-carousel-item
              >
                <div className="relative block h-full px-20 -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 text-black">
                  <div className="absolute right-2 top-2 font-bold">{i}/{props.length}</div>
                  <h1 className="font-bold text-center py-3 text-3xl">{e.bug}</h1>
                  <div className="grid gap-2">
                    <div className="text-2xl bg-[#ADE0E8] rounded-lg p-1">{e.description}</div>
                    <div className="text-2xl bg-[#ADE0E8] rounded-lg p-1">{e.timestamp}</div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
        {/* <!-- Slider controls --> */}
        <button
          type="button"
          className="absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
          data-carousel-prev
        >
          <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-800/30 group-hover:bg-gray-800/60  group-focus:ring-gray-800/70 group-focus:outline-none">
            <svg
              className="w-4 h-4 text-gray-800 rtl:rotate-180"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 6 10"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M5 1 1 5l4 4"
              />
            </svg>
            <span className="sr-only">Previous</span>
          </span>
        </button>
        <button
          type="button"
          className="absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
          data-carousel-next
        >
          <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-800/30 group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-gray-800/70 group-focus:outline-none">
            <svg
              className="w-4 h-4 text-gray-800 rtl:rotate-180"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 6 10"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m1 9 4-4-4-4"
              />
            </svg>
            <span className="sr-only">Next</span>
          </span>
        </button>
      </div>
    </>
  );
}
