package com.example.spinapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

public class SelectActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select);

        ImageButton button_high = findViewById(R.id.high_level);
        button_high.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveToMainHigh();
            }
        });

        ImageButton button_medium = findViewById(R.id.medium_level);
        button_medium.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveToMainMedium();
            }
        });

        ImageButton button_low = findViewById(R.id.low_level);
        button_low.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveToMainLow();
            }
        });
    }

    private void moveToMainHigh () {
        Intent intent_high = new Intent(SelectActivity.this, MainActivityHigh.class);
        startActivity(intent_high);
        overridePendingTransition(R.anim.fade_in, 0);
    }

    private void moveToMainMedium () {
        Intent intent_mid = new Intent(SelectActivity.this, MainActivityMedium.class);
        startActivity(intent_mid);
        overridePendingTransition(R.anim.fade_in, 0);
    }

    private void moveToMainLow () {
        Intent intent_low = new Intent(SelectActivity.this, MainActivityLow.class);
        startActivity(intent_low);
        overridePendingTransition(R.anim.fade_in, 0);
    }

    @Override
    public void onBackPressed() {
        moveTaskToBack(true);
    }
}
