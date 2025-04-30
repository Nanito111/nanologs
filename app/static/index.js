const content_container = document.getElementById("content")
const main_element = document.getElementById("content").parentElement
let headers = content_container.getElementsByTagName("h2")
let index_headings = document.getElementById("headings")

function init_headers_index() {

  for (const heading of headers) {
    let heading_from_index = document.createElement("a")
    heading_from_index.textContent = heading.textContent
    heading_from_index.href = "#" + heading.id
    index_headings.append(heading_from_index)
  }
}

init_headers_index();
main_element.onresize

let max_scroll_top = main_element.scrollHeight - main_element.clientHeight;
let scroll_factor = max_scroll_top / main_element.scrollHeight;

window.addEventListener("resize", () => {
  max_scroll_top = main_element.scrollHeight - main_element.clientHeight;
  scroll_factor = max_scroll_top / main_element.scrollHeight;
})

index_headings.children[0].className = "current-section";

main_element.onscroll = function() {
  let founded_heading_flag = false;
  for (const index_heading of index_headings.children) {
    index_heading.className = "";
  }

  for (let i = headers.length - 1; i >= 0; i--) {

    const heading_true_offset = headers[i].offsetTop + headers[i].clientHeight;
    if (scroll_factor * heading_true_offset <= main_element.scrollTop) {
      index_headings.children[i].className = "current-section";
      index_headings.children[i].scrollIntoView();
      founded_heading_flag = true;
      break;
    }
  }

  if (!founded_heading_flag) {
    index_headings.children[0].className = "current-section";
  }
}
