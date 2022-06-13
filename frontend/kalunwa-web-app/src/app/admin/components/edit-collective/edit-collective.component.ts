import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { CollectivePagesService } from '../../service/collective-pages.service';

@Component({
  selector: 'app-edit-collective',
  templateUrl: './edit-collective.component.html',
  styleUrls: ['./edit-collective.component.scss']
})
export class EditCollectiveComponent implements OnInit {
  collective: FormGroup;
  submitted= false;
  collectiveType: string | null= "project";
  isNewImage= false;
  fileName="";
  selectedCollection:any;
  collectiveId:string|null;
  profileImage:string;

  constructor(
    private formBuilder: FormBuilder,
    private service: CollectivePagesService,
    private route: ActivatedRoute,
    private router: Router,
    private snackBar: MatSnackBar
    ) { }

  ngOnInit(): void {

    this.profileImage = "../../assets/images/place.jpg";
    this.collective = this.formBuilder.group({
    title: ['',Validators.required],
    start_date: [null],
    end_date: [null],
    camp: [''],
    description: ['',Validators.required],
    meta_description: [''],
    image:[null]
    });

    this.collectiveId = this.route.snapshot.paramMap.get("id");
    this.collectiveType = this.route.snapshot.paramMap.get("collective-type");

    if(this.collectiveType == "project"){
          const editSub = this.service.getProjectDetails(this.collectiveId)
              .pipe(first())
              .subscribe(x => {
                this.selectedCollection = x;
                this.collective.patchValue(x);
                this.profileImage = x.image.image;
                editSub.unsubscribe();
              });
    }
    else if(this.collectiveType == "event"){
      const editSub = this.service.getEventDetails(this.collectiveId)
          .pipe(first())
          .subscribe(x => {
            this.selectedCollection = x;
            this.collective.patchValue(x);
            this.profileImage = x.image.image;
            editSub.unsubscribe();
          });
    }
    else if(this.collectiveType == "news"){
      const editSub =  this.service.getNewsDetails(this.collectiveId)
          .pipe(first())
          .subscribe(x => {
            this.selectedCollection = x;
            this.collective.patchValue(x);
            this.profileImage = x.image.image;
            editSub.unsubscribe();
          });
    }
    else if(this.collectiveType == "announcement"){
      const editSub =  this.service.getAnnoucement(this.collectiveId)
          .pipe(first())
          .subscribe(x => {
            this.selectedCollection = x;
            this.collective.patchValue(x);
            editSub.unsubscribe();
          });
    }
  }

  get f() { return this.collective.controls;}

  onSubmit(imageInput:any){
    this.submitted = true;

    if(this.collective.invalid){
      console.log("invalid Form");
      return;
    }

    if(this.isNewImage)
      this.processFile(imageInput);
    else if(this.collectiveType == 'announcement')
      this.updateCollective(0);
    else
      this.updateCollective(this.selectedCollection.image.id);

  }

  private updateCollective(id:number){

    let newItem:any;
    if(this.collectiveType != 'news' && this.collectiveType != 'announcement')
      newItem = {
        'title': this.f.title.value,
        'start_date': this.f.start_date.value,
        'end_date': this.f.end_date.value,
        'camp': this.f.camp.value,
        'description': this.f.description.value,
        'image': id
      };

    else if(this.collectiveType == 'news')
      newItem = {
        'title': this.f.title.value,
        'description': this.f.description.value,
        'image': id
      };

    else if(this.collectiveType == 'announcement')
    newItem = {
      'title': this.f.title.value,
      'description': this.f.description.value,
      'meta_description': this.f.meta_description.value
    };


    if(this.collectiveType=="project"){
      const addSubscribe = this.service.updateProject(newItem,this.collectiveId).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully updated ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="event"){
      const addSubscribe = this.service.updateEvent(newItem, this.collectiveId).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully updated ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="news"){
      const addSubscribe = this.service.updateNews(newItem, this.collectiveId).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully updated ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="announcement"){
      const addSubscribe = this.service.updateAnnoucement(newItem, this.collectiveId).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully updated ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
  }

  onFileChange(imageInput:any){
    this.isNewImage = true;
    const file: File = imageInput.target.files[0];
    const reader = new FileReader();
    if(!this.isFileImage(file))
      this.collective.controls["image"].setErrors({'incorrect': true});
    else{
      this.collective.controls["image"].setErrors(null);

      this.fileName = file.name;
    }


    if(imageInput.target.files && imageInput.target.files[0]){
      // File Preview
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.profileImage = reader.result as string;
      }
    }
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    if(this.isFileImage(file)){

      reader.addEventListener('load', (event: any) => {

        this.service.uploadImage(this.fileName,file).subscribe(
          (res:any) => {
            this.updateCollective(res.id);

          },
          (err) => {
            console.log("Err");
          })
        });

        reader.readAsDataURL(file);
    }
  }

  isFileImage(file: File) {
    return file && file['type'].split('/')[0] === 'image';
  }

  displayDate(date: Date){
    if(!date)
      return "";
    return this.service.printDate(date);
  }



}
