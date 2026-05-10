LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePackages
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Accord arcore-1.48 CalculatorGooglePrebuilt_85006267 CalendarGooglePrebuilt FilesPrebuilt GoogleFeedback Maps NowPlayingPrebuilt Photos RecorderPrebuilt_847964105 ScribePrebuilt_v8.4.773573318
LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
