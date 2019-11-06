package com.example.spinapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Intent;
import android.graphics.drawable.TransitionDrawable;
import android.os.Bundle;
import android.widget.ImageView;

import java.util.Timer;
import java.util.TimerTask;

public class EntryActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_entry);

        ImageView imageView = findViewById(R.id.imageView);
        TransitionDrawable transitionDrawable = (TransitionDrawable) ContextCompat.getDrawable(this, R.drawable.entry_transition);

        imageView.setImageDrawable(transitionDrawable);
        transitionDrawable.startTransition(1800);

        final Timer timer = new Timer();
        timer.schedule(new TimerTask() {

            public void run() {

                runOnUiThread(new Runnable() {

                    @Override
                    public void run() {
                        Intent in = new Intent(getApplicationContext(), SelectActivity.class);
                        startActivity(in);
                        overridePendingTransition(R.anim.fade_in, 0);
                        timer.cancel();
                    }
                });
            }
        }, 2000);
    }
}