import { ChevronDown } from "lucide-react";
import { useState } from "react";
import { html as beautifyHtml } from "js-beautify";

function SearchResult({ searchResults }: any) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  const handleToggle = (index: number) => {
    if (openIndex === index) {
      setOpenIndex(null);
    } else {
      setOpenIndex(index);
    }
  };

  return (
    <>
      <div className="mt-6 font-bold">Search Results</div>

      {searchResults.length == 0 ? (
        <p className="text-sm text-center mt-4 font-medium text-gray-300">
          No results found for your search query
        </p>
      ) : (
        ""
      )}

      {searchResults?.map((item: any, index: number) => (
        <div
          key={index}
          className="bg-white rounded-lg border px-4 py-6 mt-2 mb-2"
        >
          <div className="flex gap-1">
            <div className="flex-1">
              <p className="text-gray-800 text-sm leading-relaxed">
                {item?.properties?.content}
              </p>
            </div>
            <span className="bg-green-100 text-green-800 text-xs font-semibold px-3 py-1 rounded whitespace-nowrap h-fit">
              {Math.floor(item?.metadata?.certainty * 100)}% match
            </span>
          </div>
          <button
            onClick={() => handleToggle(index)}
            className="mt-4 flex items-center gap-1 text-blue-600 text-xs font-semibold hover:underline focus:outline-none"
          >
            <span>
              {"<>"} {"View HTML"}
            </span>
            <ChevronDown
              className={`h-4 w-4 transition-transform duration-300 ${
                openIndex === index ? "rotate-180" : ""
              }`}
            />
          </button>

          {openIndex === index && (
            <div className="mt-4 p-4 w-8/12 bg-gray-100 rounded-md text-xs text-gray-700 font-mono">
              <textarea
                className="w-full resize-none h-24 p-4 outline-none bg-gray-200 rounded"
                readOnly
                value={beautifyHtml(item?.properties?.raw_html, {
                  indent_size: 2,
                })}
              ></textarea>
            </div>
          )}
        </div>
      ))}
    </>
  );
}

export default SearchResult;
