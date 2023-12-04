/* Discard the task history and user history records from the apps. */

TRUNCATE cloud_coverage_cloudcoveragetask CASCADE;
TRUNCATE cloud_coverage_userhistory CASCADE;

TRUNCATE coastal_change_coastalchangetask CASCADE;
TRUNCATE coastal_change_userhistory CASCADE;

TRUNCATE custom_mosaic_tool_custommosaictooltask CASCADE;
TRUNCATE custom_mosaic_tool_userhistory CASCADE;

TRUNCATE fractional_cover_fractionalcovertask CASCADE;
TRUNCATE fractional_cover_userhistory CASCADE;

TRUNCATE slip_sliptask CASCADE;
TRUNCATE slip_userhistory CASCADE;

TRUNCATE spectral_anomaly_spectralanomalytask CASCADE;
TRUNCATE spectral_anomaly_userhistory CASCADE;

TRUNCATE spectral_indices_spectralindicestask CASCADE;
TRUNCATE spectral_indices_userhistory CASCADE;

TRUNCATE tsm_tsmtask CASCADE;
TRUNCATE tsm_userhistory CASCADE;

TRUNCATE urbanization_urbanizationtask CASCADE;
TRUNCATE urbanization_userhistory CASCADE;

TRUNCATE water_detection_waterdetectiontask CASCADE;
TRUNCATE water_detection_userhistory CASCADE;
