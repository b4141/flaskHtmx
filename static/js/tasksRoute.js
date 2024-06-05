function clearAllSelectedCarouselCalendarWeek() {
  let allcalendarDivisions = document.getElementsByClassName("tasks-table-calendar-division");
  for (element of allcalendarDivisions) {
    element.classList.remove("active")
  }
}

function getSelectedCarouselCalendarWeek() {
  let allcalendarDivisions = document.getElementsByClassName("tasks-table-calendar-division");
  for (element of allcalendarDivisions) {
    if (element.classList.contains("active")) {
      return element
    }
  }
}

function nextCarouselCalendarWeek() {
  let selectedDivision = parseInt(getSelectedCarouselCalendarWeek().getAttribute("division"));
  clearAllSelectedCarouselCalendarWeek();
  if (selectedDivision < 4) {
    selectedDivision += 1;
  }
  document.getElementById(`calendar-division-${selectedDivision}`).classList.add("active")
}
function prevCarouselCalendarWeek() {
  let selectedDivision = parseInt(getSelectedCarouselCalendarWeek().getAttribute("division"));
  clearAllSelectedCarouselCalendarWeek();
  if (selectedDivision > 1) {
    selectedDivision -= 1;
  }
  document.getElementById(`calendar-division-${selectedDivision}`).classList.add("active")
}
