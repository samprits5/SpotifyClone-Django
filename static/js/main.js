Object.defineProperty(HTMLMediaElement.prototype, 'playing', {
    get: function () {
        return !!(this.currentTime > 0 && !this.paused && !this.ended && this.readyState > 2);
    }
})
$(document).ready(function () {
    const $musicPlayer = document.getElementById('musicPlayer');
    if ($musicPlayer != null) {
        (function () {
            /*----------------------------
                    Play / Pause Toggle
                ------------------------------*/
            function play() {
                if ($('#play').hasClass('pause')) {
                    $musicPlayer.pause()
                } else {
                    $musicPlayer.play()
                }
                $('#play').toggleClass('pause');
            }
            $('#play').click(play);
            /*-----------------------------------------------
                Convert Audio Duration (Sec) into MM : SS
            ------------------------------------------------*/
            function getDurMin($sec) {
                // if($sec.isNaN()){}
                var min = parseInt($sec / 60);
                var sec = parseInt($sec % 60);
                if (min < 10) {
                    min = '0' + min;
                }
                if (sec < 10) {
                    sec = '0' + sec;
                }
                return { min: min, sec: sec };
            }
            /*-----------------------------------------------
                Update duration into DOM in MM : SS format
            ------------------------------------------------*/
            var curTime = getDurMin($musicPlayer.currentTime),
                totDur = getDurMin($musicPlayer.duration);
            $(function () {
                $("#startTime").text(curTime.min + " : " + curTime.sec)
            })
            /*-----------------------------------------------
                Repeat Control Starts
            ------------------------------------------------*/
            $('#repeat').click(function () {
                // if (!$musicPlayer.playing) { play() }
                if ($(this).hasClass('looped')) {
                    $musicPlayer.loop = false
                    $(this).removeClass('looped')
                } else {
                    $musicPlayer.loop = true
                    $(this).addClass('looped')
                }
            })

            /*-----------------------------------------------
                Repeat Control Ends
            ------------------------------------------------*/
            /*-----------------------------------------------
                Volume Control Starts
            ------------------------------------------------*/
            const $vol_icon = $('#volume-icon'),
                $vol_thumb = $('#volume-range-thumb'),
                $vol_bar = $('#volume-range-bar'),
                $vol_parent = $('#volume-range'),
                $vol_main = $('#volume-range-main');
            // Set Volume using 'data-value' attribute.
            function setVol() {
                if (typeof $vol_bar.attr('data-value') != 'undefined') {
                    $musicPlayer.volume = (parseInt($vol_bar.attr('data-value')) / 100)
                }
            }
            // Update Volume
            function updateVol() {
                var calcVol = ($musicPlayer.volume * $vol_parent.width());
                $vol_bar.width(calcVol)
                if (calcVol <= $vol_thumb.width() / 2) {
                    $vol_thumb.css({
                        'left': '0'
                    })
                } else {
                    $vol_thumb.css({
                        'left': calcVol - $vol_thumb.width() / 2
                    })
                }
                if ($musicPlayer.volume == 0) {
                    $vol_icon.addClass('muted')
                }
                else {
                    $vol_icon.removeClass('muted')
                }
            }
            // Toggle mute on click icon
            $vol_icon.click(function () {
                $(this).toggleClass('muted');
                if ($(this).hasClass('muted')) {
                    $musicPlayer.volume = 0
                } else {
                    // setThumb('#volume-range-thumb', '#volume-range-main');
                    $musicPlayer.volume = (parseInt($vol_bar.attr('data-value')) / 100)
                }
            });
            // Set icon according to volume.
            $musicPlayer.onvolumechange = updateVol;
            updateVol()
            // Set volume accordingly when clicked anywhere on the range bar
            $vol_main.click(function (e) {
                e.stopPropagation()
                var posX = e.pageX - $(this).offset().left;
                $vol_bar.attr('data-value', ((posX / $(this).width()) * 100));
                setVol();
            });
            // Make thumb draggable
            $vol_thumb.draggable({
                axis: 'x',
                drag: function () {
                    var posX = ($(this).position().left + $(this).width() / 2);
                    if (posX <= $(this).width() / 2) {
                        posX = 0
                    }
                    $vol_bar.attr('data-value', parseInt((posX / $vol_parent.width()) * 100));
                    $vol_bar.width((posX / $vol_parent.width()) * 100)
                    $musicPlayer.volume = (posX / $vol_parent.width())
                    if (posX >= $vol_parent.width()) {
                        $musicPlayer.volume = 1
                    } else {
                        $musicPlayer.volume = (posX / $vol_parent.width())
                    }
                },
                containment: [
                    ($vol_parent.offset().left), // x0
                    0,//y0
                    (($vol_parent.offset().left //<-->
                        + $vol_parent.width())  //<--x1-->
                        - ($vol_thumb.width() / 2)),//<-->
                    0//y1
                ]
            })
            /*-----------------------------------------------
                Volume Control Ends
            ------------------------------------------------*/
            /*-----------------------------------------------
                Duration Control Starts
            ------------------------------------------------*/
            const $dur_thumb = $('#duration-range-thumb'),
                $dur_bar = $('#duration-range-bar'),
                $dur_main = $('#duration-range-main'),
                $dur_parent = $('#duration-range');

            // Set duration accordingly when clicked anywhere on the range bar
            $dur_main.click(function (e) {
                e.stopPropagation()
                var posX = e.pageX - $(this).offset().left;
                $musicPlayer.currentTime = (posX / $dur_parent.width()) * $musicPlayer.duration;
            })
            // Updates range bar and time (MM : SS) in DOM when playing
            $musicPlayer.ontimeupdate = function () {
                $("#startTime").text(getDurMin(this.currentTime).min + " : " + getDurMin(this.currentTime).sec)
                var curTime = parseInt(this.currentTime)
                var totalTime = parseInt(this.duration);
                var calcPos = ($dur_parent.width() * (curTime / totalTime))
                $dur_bar.width(calcPos)
                if (calcPos <= ($dur_thumb.width() / 2)) {
                    $dur_thumb.css({
                        'left': '0'
                    })
                }
                //    else if (calcPos >= ($dur_parent.width() - $dur_thumb.width())) {
                //         $dur_thumb.css({
                //             'left': ($dur_parent.width() - $dur_thumb.width())
                //         })
                //     }
                else {
                    $dur_thumb.css({
                        'left': calcPos - ($dur_thumb.width() / 2)
                    })
                }
                if ($musicPlayer.playing) {
                    $('#play').addClass('pause')
                } else {
                    $('#play').removeClass('pause')
                }
            }
            // Drag thumb
            var calcDur;
            $dur_thumb.draggable({
                axis: 'x',
                start: function () {
                    $musicPlayer.pause()
                },
                drag: function () {
                    $dur_bar.width(($(this).position().left + ($(this).width() / 2)));
                    calcDur = ($dur_bar.width() / $dur_parent.width()) * $musicPlayer.duration
                    $("#startTime").text(getDurMin(calcDur).min + " : " + getDurMin(calcDur).sec);
                },
                stop: function () {
                    $musicPlayer.currentTime = calcDur
                    $musicPlayer.play();
                },
                containment: [
                    ($dur_parent.offset().left), // x0
                    0,//y0
                    (($dur_parent.offset().left //<-->
                        + $dur_parent.width())  //<--x1-->
                        + $dur_thumb.width() / 2),//<-->
                    0//y1
                ]
            })
            /*-----------------------------------------------
                Duration Control Ends
            ------------------------------------------------*/

            // others
            $('#addToFav').click(function () {
                $(this).toggleClass('inFav');
            });
        })();
    }
    function isUniqueId() {
        $('[id]').each(function () {
            var ids = $('[id="' + this.id + '"]');
            if (ids.length > 1 && ids[0] == this)
                console.warn('Multiple IDs #' + this.id);
        });
    }
    isUniqueId();

    $(window).scroll(function () {
        if ($('#header-index').length > 0) {
            if ($(this).scrollTop() > 0) {
                $('#header-index').addClass('header-fix')
            } else {
                $('#header-index').removeClass('header-fix')

            }
        }
    })
    function checkSvg() {
        if ($('.section-menu-user-img').length > 0) {
            ($('.section-menu-user-img').children('img').attr('src').indexOf('svg') != -1)
                ? ($('.section-menu-user-img').css({
                    'overflow': 'visible'
                }))
                : ($('.section-menu-user-img').css({
                    'overflow': 'hidden'
                }))
        }
    }
    checkSvg();
    function getImgName() {
        var filename;
        $('#addUserImg').change(function () {
            filename = $(this).val();
            filename = filename.substring(filename.lastIndexOf('\\') + 1);
            $(this).siblings('img').attr('src' , './images/' + filename);
            checkSvg();
        });
    }
    getImgName();
});