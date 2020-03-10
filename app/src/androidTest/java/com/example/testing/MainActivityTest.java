package com.example.testing;

import android.app.Activity;
import android.app.Instrumentation;
import android.view.View;

import androidx.test.internal.runner.junit4.AndroidJUnit4ClassRunner;
import androidx.test.rule.ActivityTestRule;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.platform.app.InstrumentationRegistry.getInstrumentation;
import static org.junit.Assert.*;


public class MainActivityTest {
    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<MainActivity>(MainActivity.class);
    private MainActivity mActivity = null;

    Instrumentation.ActivityMonitor monitor = getInstrumentation().addMonitor(SecondaryActivity.class.getName(),null,false);

    @Before
    public void setUp() throws Exception {
        mActivity= mActivityTestRule.getActivity();
    }

    @Test
    public void TestLaunch(){
        View view = mActivity.findViewById(R.id.activity_main_title);
        assertNotNull(view);
    }

    @Test
    public void TestLaunchOfSecondActivityOnButtonClick(){

        assertNotNull(mActivity.findViewById(R.id.button_next_activity));
        onView(withId(R.id.button_next_activity)).perform(click());
        Activity secondActivity = getInstrumentation().waitForMonitorWithTimeout(monitor,5000);
        assertNotNull(secondActivity);
        secondActivity.finish();
    }

    @After
    public void tearDown() throws Exception {
        mActivity=null;
    }
}