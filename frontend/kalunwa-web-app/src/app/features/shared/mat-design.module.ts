import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import {MatMenuModule} from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatCardModule} from '@angular/material/card';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatPaginatorModule, PageEvent} from '@angular/material/paginator';
import {MatChipsModule} from '@angular/material/chips';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatDialogModule} from '@angular/material/dialog';
import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import { NgImageSliderModule } from 'ng-image-slider';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';

const MATERIAL = [
  MatToolbarModule,
  MatButtonModule,
  MatMenuModule,
  MatIconModule,
  MatSidenavModule,
  MatCardModule,
  MatButtonToggleModule,
  MatPaginatorModule,
  MatChipsModule,
  MatAutocompleteModule,
  MatDialogModule,
  MatInputModule,
  MatSelectModule,
  NgImageSliderModule,
  MatProgressSpinnerModule,
  MatCheckboxModule,
  MatDatepickerModule,
  MatNativeDateModule,
  MatFormFieldModule,
  BrowserAnimationsModule,
  BrowserModule
];

@NgModule({
  declarations: [],
  exports: [MATERIAL],
  imports: [
    CommonModule,
    MATERIAL
  ]
})
export class MatDesignModule { }
