/**
 * Created by Mayur Gupta on 22-07-2017.
 */
//create a summary in the panel heading based on the input values
$('.panel-collapse').on('hide.bs.collapse', function(e) {
  var arrBuf = [];
  var anchorTarget = $('[href="#' + e.currentTarget.id + '"]');

  //store the original heading
  anchorTarget.data('orig-text', anchorTarget.text());

  //create the output
  //you can modify the formatting of the code to output a more
  //responsive summary
  $('.form-control', e.currentTarget).each(function() {
    if (this.value !== '' && this.value !== '....') {
      arrBuf.push(this.value);
    }
  });

  if (arrBuf.length > 0) {
    anchorTarget.html(arrBuf.join(', '));
  }
  //end output
});

//restore the original text
$('.panel-collapse').on('show.bs.collapse', function(e) {
  var anchorTarget = $('[href="#' + e.currentTarget.id + '"]');
  anchorTarget.html(anchorTarget.data('orig-text'));

  $('.form-control', e.currentTarget).first().attr("autofocus", "autofocus");

   $('.form-control', e.currentTarget).first().focus();

});

$('[type="submit"]').on('click', function(e) {
  alert('Application Sent, Successfully!');
})

$(document).ready(function() {
    function adjustIframeHeight() {
        var $body   = $('body'),
            $iframe = $body.data('iframe.fv');
        if ($iframe) {
            // Adjust the height of iframe
            $iframe.height($body.height());
        }
    }

    // IMPORTANT: You must call .steps() before calling .formValidation()
    $('#profileForm')
        .steps({
            headerTag: 'h2',
            bodyTag: 'section',
			autoFocus: true,
			enableContentCache: true,
			transitionEffect: 'fade',
			transitionEffectSpeed: 170,
            onStepChanged: function(e, currentIndex, priorIndex) {
                // You don't need to care about it
                // It is for the specific demo
                adjustIframeHeight();
            },
            // Triggered when clicking the Previous/Next buttons
            onStepChanging: function(e, currentIndex, newIndex) {
                var fv         = $('#profileForm').data('formValidation'), // FormValidation instance
                    // The current step container
                    $container = $('#profileForm').find('section[data-step="' + currentIndex +'"]');

                // Validate the container
                fv.validateContainer($container);

                var isValidStep = fv.isValidContainer($container);
                if (isValidStep === false || isValidStep === null) {
                    // Do not jump to the next step
                    return false;
                }

                return true;
            },
            // Triggered when clicking the Finish button
            onFinishing: function(e, currentIndex) {
                var fv         = $('#profileForm').data('formValidation'),
                    $container = $('#profileForm').find('section[data-step="' + currentIndex +'"]');

                // Validate the last step container
                fv.validateContainer($container);

                var isValidStep = fv.isValidContainer($container);
                if (isValidStep === false || isValidStep === null) {
                    return false;
                }

                return true;
            },
            onFinished: function(e, currentIndex) {
                // Uncomment the following line to submit the form using the defaultSubmit() method
                // $('#profileForm').formValidation('defaultSubmit');

                // For testing purpose
                $('#welcomeModal').modal();
            }
        })
        .formValidation({
            framework: 'bootstrap',
            icon: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            // This option will not ignore invisible fields which belong to inactive panels
            exclude: ':disabled',
            fields: {
                tr: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				work: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				workd: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				pre: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				product: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				completion: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				loc: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				pin: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				pub: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				sale: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				end: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				seek: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				seek1: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				bid: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				bid1: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				bid2: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                },
				bid3: {
                    validators: {
                        notEmpty: {
                            message: 'The field is required'
                        }
                    }
                }
            }
        });
});