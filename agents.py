import sys
from core.activity_tracker import ActivityTracker
from core.screenshot_manager import ScreenshotManager
from core.instance_manager import InstanceManager
from core.config_manager import ConfigManager

def main():
    # Ensure only one instance is running
    InstanceManager.check_instance()

    try:
        # Initialize components
        config_manager = ConfigManager()
        activity_tracker = ActivityTracker()
        screenshot_manager = ScreenshotManager(
            blur=config_manager.get_config('blur_screenshots'),
            interval=config_manager.get_config('screenshot_interval')
        )

        try:
            UploadManager = UploadManager(
                aws_access_key=config_manager.get_config('aws_access_key'),
                aws_secret_key=config_manager.get_config('aws_secret_key'),
                bucket_name=config_manager.get_config('s3_bucket_name')
            )
        except Exception as e:
            print(f"Error initializing UploadManager: {e}")
            sys.exit(1)

        try:
            TimeZoneManager = TimeZoneManager()
        except Exception as e:
            print(f"Error initializing TimeZoneManager: {e}")
            sys.exit(1)

        # Start tracking and capturing
        activity_tracker.start_tracking()
        screenshot_manager.start_screenshot_loop()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    finally:
        # Clean up and release instance lock
        InstanceManager.release_instance()

if __name__ == "__main__":
    main()