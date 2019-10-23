var oldAudio;

var stateID = 0;

$(document).ready(function(){
      $('#sidebarCollapse').on('click', function () {
          $('#sidebar').toggleClass('active');
      });
  });

function endAudio(){
  $('#speaker-anim-'+stateID).removeClass('show-gif');
  $('#speaker-anim-'+stateID).addClass('hide-gif');
  $('#span'+stateID).text('Play');
}

function playmusic(id) {

  if(stateID == 0){

    var audio = document.getElementById("audio"+id);

    oldAudio = audio;

    stateID = id;

    audio.play();

    $('#span'+id).text('Pause');
    $('#speaker-anim-'+id).removeClass('hide-gif');
      $('#speaker-anim-'+id).addClass('show-gif');

  } else if(stateID != id){

    if(oldAudio.duration > 0 && !oldAudio.paused){
      
      oldAudio.pause();
      // oldAudio.currentTime = 0;
      $('#span'+stateID).text('Play');
      
      $('#speaker-anim-'+stateID).removeClass('show-gif');

      $('#speaker-anim-'+stateID).addClass('hide-gif');


      var audio = document.getElementById("audio"+id);

      oldAudio = audio;

      stateID = id;

      audio.play();

      $('#span'+id).text('Pause');
      $('#speaker-anim-'+id).removeClass('hide-gif');
      $('#speaker-anim-'+id).addClass('show-gif');

    } else {

      var audio = document.getElementById("audio"+id);

      oldAudio = audio;

      stateID = id;

      audio.play();

      $('#span'+id).text('Pause');
      $('#speaker-anim-'+id).removeClass('hide-gif');
      $('#speaker-anim-'+id).addClass('show-gif');

    }

  } else {

    if(oldAudio.duration > 0 && !oldAudio.paused){

      oldAudio.pause();
      // oldAudio.currentTime = 0;
      $('#span'+stateID).text('Play');

      $('#speaker-anim-'+stateID).removeClass('show-gif');
      $('#speaker-anim-'+stateID).addClass('hide-gif');

    } else {

      var audio = document.getElementById("audio"+id);

      oldAudio = audio;

      stateID = id;

      audio.play();

      $('#span'+id).text('Pause');
      $('#speaker-anim-'+id).removeClass('hide-gif');
      $('#speaker-anim-'+id).addClass('show-gif');

    }
  }

}


function triggerModal(){

        $('#exampleModal').modal();
    }



