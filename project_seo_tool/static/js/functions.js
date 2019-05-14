
/*
Modal Functionalitiy
*/

function openCustomModal(url) {
  $('#custom-modal').load(url, function() {
    $(this).modal('show');
  });
  return false;
}

function closeCustomModal() {
  $('#custom-modal').modal('hide');
  return false;
}
