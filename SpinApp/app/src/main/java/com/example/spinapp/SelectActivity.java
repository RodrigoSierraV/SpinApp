package com.example.spinapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class SelectActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select);

        Button button_high = findViewById(R.id.high_cadence);
        button_high.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveToMainHigh();
            }
        });

        Button button_medium = findViewById(R.id.medium_cadence);
        button_medium.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveToMainMedium();
            }
        });

        Button button_low = findViewById(R.id.low_cadence);
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
    }

    private void moveToMainMedium () {
        Intent intent_mid = new Intent(SelectActivity.this, MainActivityMedium.class);
        startActivity(intent_mid);
    }

    private void moveToMainLow () {
        Intent intent_low = new Intent(SelectActivity.this, MainActivityLow.class);
        startActivity(intent_low);
    }
}
