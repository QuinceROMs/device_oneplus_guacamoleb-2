LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePackages
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := arcore CalculatorGooglePrebuilt_85011599 CalendarGooglePrebuilt FilesPrebuilt GoogleFeedback Photos RecorderPrebuilt_847964105 ScribePrebuilt_v8.7.880674799
LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
